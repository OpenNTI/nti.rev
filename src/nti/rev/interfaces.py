#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import interface

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from nti.schema.field import Bool
from nti.schema.field import List
from nti.schema.field import Text
from nti.schema.field import Choice
from nti.schema.field import Number
from nti.schema.field import Object
from nti.schema.field import HTTPURL
from nti.schema.field import DateTime
from nti.schema.field import TextLine
from nti.schema.field import ValidURI


class IRevClient(interface.Interface):
    """
    Handles Rev order operations
    """

    def upload_source_file(source_file):
        """
        Upload a source file to be used in an order.
        
        FIXME: documentation - input, output, expected error cases and what exceptions might be raised
        """

    def submit_transcription_order(order):
        """
        Submit a new transcription order.
        """

    def submit_caption_order(order):
        """
        Submit a new caption order.
        """

    def get_order(ordernum):
        """
        Get detailed information about a specific order.
        """

    def get_orders():
        """
        Get paged list of orders for user.
        
        FIXME: take inputs, define them with default args so they don't have to be specified (use Rev default args)
        """

    def cancel_order(ordernum):
        """
        Cancel an order.
        """

    def get_attachment(attachment_id):
        """
        Get metadata about an order attachment.
        """

    def get_attachment_content(attachment_id):
        """
        Get the raw data for the attachment with given ID.
        """


class ICredentials(interface.Interface):
    """
    Security and authentication keys used to access the Rev API
    
    # FIXME: Split into two different interfaces IClientKey, IUserKey, and shared interface
    """

    client_API_key = TextLine(title=u'The client API key',
                              description=u"""This is a secret key specific to each partner 
                              that wishes to use the Rev API.""",
                              required=True)

    user_API_key = TextLine(title=u'The user API key',
                            description=u"""This is a secret key specific to a Rev user, 
                            which identifies the user account under whose privileges 
                            the requested operation executes.""",
                            required=True)


class ISourceFileUpload(interface.Interface):
    """
    Describes a media source file to be retrieved, uploaded, and used in an order.
    """

    content_type = TextLine(title=u'The content type of the media to be retrieved',
                            description=u"""If not specified, Rev will try to determine the content type
                            from the server response.""",
                            required=False)

    filename = TextLine(title=u'The filename for the media',
                        description=u"""If not specified, Rev will try to determine the filename 
                        from the URL.""",
                        required=False)

    url = HTTPURL(title=u'The URL where the media can be retrieved',
                  description=u"""The URL must be publicly accessible. 
                  HTTPS URLs are ok as long as the site in question has a valid certificate,""",
                  required=True)


class IInput(interface.Interface):
    """
    An order input file to be captioned or transcribed
    """


class ISourceFileInput(IInput):
    """
    An order input for a source file that has already been uploaded to be used in an order
    """

    audio_length_seconds = Number(title=u'The length of the audio (in seconds, rounded up)',
                                  description=u"""If the URI is for media stored in an S3 bucket,
                                  Rev will try to calculate the audio length automatically.""",
                                  required=False)

    uri = ValidURI(title=u'A URI identifying the uploaded media',
                   required=True)


class IExternalLinkInput(IInput):
    """
    An order input for an external link to a file
    """

    audio_length_seconds = Number(title=u'The length of the audio (in seconds, rounded up)',
                                  description=u"""If external link is a YouTube URL, 
                                  audio length is determined automatically.""",
                                  required=False)

    external_link = HTTPURL(title=u'The external link URL',
                            required=True)


class ISpeaker(interface.Interface):
    """
    A speaker
    """

    id = Number(title=u'The ID of the speaker',
                required=True)

    name = TextLine(title=u'The name of the speaker',
                    required=True)


class ISpeakers(interface.Interface):
    """
    The attachment speakers
    """

    speakers = List(value_type=Object(ISpeaker),
                    title=u'A list of speakers',
                    required=True)


MONOLOGUE_ELEMENT_TYPE_TAG = u'tag'
MONOLOGUE_ELEMENT_TYPE_TEXT = u'text'

MONOLOGUE_ELEMENT_TYPE_ITEMS = (MONOLOGUE_ELEMENT_TYPE_TEXT,
                                MONOLOGUE_ELEMENT_TYPE_TAG)

MONOLOGUE_ELEMENT_TYPE_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in MONOLOGUE_ELEMENT_TYPE_ITEMS]
)


class IMonologueElement(interface.Interface):
    """
    Each element of a monologue is either text (transcribed speech)
    or a tag (an annotation), such as inaudible or crosstalk.
    """

    type = Choice(vocabulary=MONOLOGUE_ELEMENT_TYPE_VOCABULARY,
                  title=u'The type of the monologue element',
                  required=True)

    value = Text(title=u'The value of the monologue element',
                 description=u"""For text elements, value contains the text.
                 For tag elements, value contains the annotation type.""",
                 required=True)

    #: Timestamp format is hh:mm:sss,fff
    #: where fff represents milliseconds
    #: Text elements may or may not contain a timestamp.
    #: Tag elements require a timestamp.

    # FIXME: schema?
    # FIXME: Indicate required for tag elements but not required for text
    # elements
    # FIXME: Internally datetime object
    timestamp = TextLine(title=u'The timestamp')


class IMonologueElements(interface.Interface):
    """
    Elements of a monologue.
    """

    elements = List(value_type=Object(IMonologueElement),
                    title=u'A list of monologue elements',
                    required=True)


class IMonologue(interface.Interface):
    """
    A monologue (transcribed speech).
    Each monologue corresponds to a run of text from one speaker.
    """

    id = Number(title=u'The ID of the monologue',
                required=True)

    # FIXME: Indicate speaker must be one of the speakers from the attachment content's ISpeakers
    # This speaker ID is the same as the ISpeaker id
    speaker = Number(title=u'The ID of the speaker',
                     required=True)

    # FIXME: Indicate speaker must be one of the speakers from the attachment content's ISpeakers
    # This speaker_name is the same as the ISpeaker name
    speaker_name = TextLine(title=u'The name of the speaker',
                            required=True)

    elements = Object(schema=IMonologueElements,
                      title=u'Elements of the monologue',
                      required=True)


class IMonologues(interface.Interface):
    """
    The attachment monologues (transcribed speech)
    """

    monologues = List(value_type=Object(IMonologue),
                      title=u'A list of monologues',
                      required=True)


class IComment(interface.Interface):
    """
    A comment on an order
    """

    by = TextLine(title=u'The author of the comment',
                  required=True)

    timestamp = DateTime(title=u'The date and time the comment was made. in UTC',
                         required=True)

    text = Text(title=u'The text of the comment',
                required=True)


NOTIFICATION_FINAL_ONLY = u'(the default) A notification is sent only when the order is complete'
NOTIFICATION_DETAILED = u'A notification is sent whenever the order is in a new status or has a new comment'

NOTIFICATION_ITEMS = (NOTIFICATION_DETAILED,
                      NOTIFICATION_FINAL_ONLY)

NOTIFICATION_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in NOTIFICATION_ITEMS]
)


class INotification(interface.Interface):
    """
    Options specified when placing a request for an order 
    to enable receiving notifications about the order status
    """

    url = HTTPURL(title=u'The URL where updates will be posted',
                  required=True)

    level = Choice(vocabulary=NOTIFICATION_VOCABULARY,
                   title=u'Specifies which notifications are sent',
                   required=False)

# FIXME? nti.interfaces ILinks (leave for now), might change into NTILinks
class ILink(interface.Interface):
    """
    Link with URL of the resource for getting attachment content
    """

    # Likely, rel="content"
    rel = TextLine(title=u'The relationship between the current document and the linked document',
                   required=True)

    href = TextLine(title=u'The URL of the link',
                    required=True)


class ILinks(interface.Interface):
    """
    Links with URLs of the resource for getting attachment content
    """

    links = List(value_type=Object(ILink),
                 title=u'A list of links with URLs of the resource for getting attachment content',
                 required=True)


ATTACHMENT_KIND_MEDIA = u'media'
ATTACHMENT_KIND_CAPTION = u'caption'
ATTACHMENT_KIND_TRANSCRIPT = u'transcript'

ATTACHMENT_KIND_ITEMS = (ATTACHMENT_KIND_MEDIA,
                         ATTACHMENT_KIND_TRANSCRIPT,
                         ATTACHMENT_KIND_CAPTION)

ATTACHMENT_KIND_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in ATTACHMENT_KIND_ITEMS]
)


class IAttachment(interface.Interface):
    """
    An attachment
    """

    kind = Choice(vocabulary=ATTACHMENT_KIND_VOCABULARY,
                  title=u'The kind of attachment',
                  required=True)
    #FIXME: filename (name is not descriptive) but leave for now
    name = TextLine(title=u'Filename for the attachment',
                    required=True)

    id = TextLine(title=u'ID for the attachment',
                  required=True)

    # FIXME: Indicate this attribute is only included if kind="transcript"
    audio_length_seconds = Number(title=u'The length (in seconds) of the audio attachment',
                                  required=False)

    links = Object(schema=ILinks,
                   title=u'A list of links with URLs of the resource for getting attachment content',
                   required=True)


class IAttachments(interface.Interface):
    """
    A list of attachments
    """

    attachments = List(value_type=Object(IAttachment),
                       title=u'A list of attachments',
                       required=True)


class IAttachmentContent(interface.Interface):
    """
    The content of the attachment
    """

    speakers = Object(schema=ISpeakers,
                      title=u'The speakers',
                      required=True)

    monologues = Object(schema=IMonologues,
                        title=u'The monologues (transcribed speech)',
                        description=u"""Each monologue corresponds to a run of text from one speaker.""",
                        required=True)


class IOrderRequest(interface.Interface):
    """
    An object providing information for placing an order
    """
    client_ref = TextLine(title=u'A reference number for the order meaningful to the client',
                          required=False)

    notification = Object(schema=INotification,
                          title=u'Enables receiving notifications about the order status',
                          required=False)


#: Completed and Cancelled are the only status values guaranteed not to
#: change in v1 of the API.


ORDER_STATUS_COMPLETED = u'Completed'
ORDER_STATUS_CANCELLED = u'Cancelled'
ORDER_STATUS_CAPTIONING = u'Captioning'
ORDER_STATUS_IN_PROGRESS = u'In Progress'
ORDER_STATUS_TRANSCRIBING = u'Transcribing'

ORDER_STATUS_ITEMS = (ORDER_STATUS_TRANSCRIBING,
                      ORDER_STATUS_CAPTIONING,
                      ORDER_STATUS_IN_PROGRESS,
                      ORDER_STATUS_COMPLETED,
                      ORDER_STATUS_CANCELLED)

ORDER_STATUS_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in ORDER_STATUS_ITEMS]
)


class IOrderDetails(interface.Interface):
    """
    The details of an order
    """

    order_number = TextLine(title=u'Rev assigned order number',
                            required=True)

    client_ref = TextLine(title=u'The client reference order number provided with the order request',
                          required=True)

    # TODO: Rounded to the nearest whole dollar? Convert to cents?
    # Probably fractional, rounded to two decimal places
    # "The price unit in Dollars and it shows default order price" what does default order price mean?
    price = Number(title=u'Total cost of the order (in dollars)',
                   required=True)

    status = Choice(vocabulary=ORDER_STATUS_VOCABULARY,
                    title=u'The status of the order',
                    required=True)

    attachments = List(value_type=Object(IAttachment),
                       title=u'The attachments with the order',
                       required=True)

    comments = List(value_type=Object(IComment),
                    title=u'The comments on the order',
                    required=True)


class IOrder(IOrderRequest, IOrderDetails):
    """
    An order
    """


class IOrders(interface.Interface):
    """
    A list of orders
    """

    orders = List(value_type=Object(IOrder),
                  title=u'A list of orders',
                  required=True)


class ITranscriptionOptions(interface.Interface):
    """
    Information specified when placing a transcription order that
    provides information on what needs to be transcribed and 
    sets other transcription options
    """

    # TODO: Indicate inputs must have at least one element
    inputs = List(value_type=Object(IInput),
                  title=u'A list of media to transcribe',
                  required=True)

    # TODO: What is the default value for when this field is not included?
    verbatim = Bool(title=u'Transcribe the provided files verbatim',
                    description=u"""If true, all filler words (i.e. umm, huh) will be included""",
                    required=False)

    # TODO: What is the default value for when this field is not included?
    timestamps = Bool(title=u'Include timestamps',
                      required=False)


class ITranscriptionOrderRequest(IOrderRequest):
    """
    An object providing information for placing a transcription order
    """

    transcription_options = Object(schema=ITranscriptionOptions,
                                   title=u'Transcription options for a transcription order',
                                   description=u"""Provides information on what needs to be transcribed 
                                   and allows for any transcription options to be set""",
                                   required=True)

# FIXME: Ambiguous name?


class ICaption(interface.Interface):
    """
    Caption details for a caption order
    including total length of the audio of media attachments for the order
    """

    total_length_seconds = Number(title=u'The total length (in seconds) of the videos included in the caption order',
                                  required=True)


class ICaptionOrderDetails(IOrderDetails):
    """
    The details of a caption order
    """

    caption = Object(schema=ICaption,
                     title=u'Caption details for the caption order',
                     description=u"""Total length (in seconds) of the videos included in the caption order""",
                     required=True)


OUPUT_FILE_FORMAT_DFXP = u'Dfxp'
OUPUT_FILE_FORMAT_SUBRIP = u'SubRip'
OUPUT_FILE_FORMAT_SCENARIST = u'Scc'
OUPUT_FILE_FORMAT_WEB_VTT = u'WebVtt'
OUPUT_FILE_FORMAT_MAC_CAPTION = u'Mcc'
OUPUT_FILE_FORMAT_TIMED_TEXT = u'Ttml'
OUPUT_FILE_FORMAT_TRANSCRIPT = u'Transcript'
OUPUT_FILE_FORMAT_CHEETAH_CAP = u'CheetahCap'
OUPUT_FILE_FORMAT_SPRUCE_SUBTITLE_FILE = u'Stl'
OUPUT_FILE_FORMAT_QUICKTIME_TIMED_TEXT = u'QTtext'
OUPUT_FILE_FORMAT_AVID_DS_SUBTITLE_FILE = u'AvidDs'
OUPUT_FILE_FORMAT_FACEBOOK_READY_SUBRIP = u'FacebookSubRip'

OUPUT_FILE_FORMAT_ITEMS = (OUPUT_FILE_FORMAT_SUBRIP,
                           OUPUT_FILE_FORMAT_SCENARIST,
                           OUPUT_FILE_FORMAT_MAC_CAPTION,
                           OUPUT_FILE_FORMAT_TIMED_TEXT,
                           OUPUT_FILE_FORMAT_QUICKTIME_TIMED_TEXT,
                           OUPUT_FILE_FORMAT_TRANSCRIPT,
                           OUPUT_FILE_FORMAT_WEB_VTT,
                           OUPUT_FILE_FORMAT_DFXP,
                           OUPUT_FILE_FORMAT_CHEETAH_CAP,
                           OUPUT_FILE_FORMAT_SPRUCE_SUBTITLE_FILE,
                           OUPUT_FILE_FORMAT_AVID_DS_SUBTITLE_FILE,
                           OUPUT_FILE_FORMAT_FACEBOOK_READY_SUBRIP)

OUTPUT_FILE_FORMAT_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in OUPUT_FILE_FORMAT_ITEMS]
)


#: Rev also has translators in many other languages with limited capacity.
#: Please contact Rev at support@rev.com with your unique needs.

SUBTITLE_LANGUAGE_DUTCH = u'nl'
SUBTITLE_LANGUAGE_ARABIC = u'ar'
SUBTITLE_LANGUAGE_FRENCH = u'fr'
SUBTITLE_LANGUAGE_GERMAN = u'de'
SUBTITLE_LANGUAGE_ITALIAN = u'it'
SUBTITLE_LANGUAGE_RUSSIAN = u'ru'
SUBTITLE_LANGUAGE_SPANISH = u'es'
SUBTITLE_LANGUAGE_PORTUGUESE_BRAZIL = u'pt-br'
SUBTITLE_LANGUAGE_CHINESE_SIMPLIFIED = u'zh-si'
SUBTITLE_LANGUAGE_CHINESE_TRADITIONAL = u'zh-tr'


SUBTITLE_LANGUAGE_ITEMS = (SUBTITLE_LANGUAGE_ARABIC,
                           SUBTITLE_LANGUAGE_CHINESE_SIMPLIFIED,
                           SUBTITLE_LANGUAGE_CHINESE_TRADITIONAL,
                           SUBTITLE_LANGUAGE_DUTCH,
                           SUBTITLE_LANGUAGE_FRENCH,
                           SUBTITLE_LANGUAGE_GERMAN,
                           SUBTITLE_LANGUAGE_ITALIAN,
                           SUBTITLE_LANGUAGE_PORTUGUESE_BRAZIL,
                           SUBTITLE_LANGUAGE_RUSSIAN,
                           SUBTITLE_LANGUAGE_SPANISH)

SUBTITLE_LANGUAGE_VOCABULARY = SimpleVocabulary(
    [SimpleTerm(_x) for _x in SUBTITLE_LANGUAGE_ITEMS]
)


class ICaptionOptions(interface.Interface):
    """
    Information specified when placing a caption order that
    provides information on what needs to be captioned and 
    specifies the desired captions output format
    """

    # TODO: Indicate inputs must have at least one element
    inputs = List(value_type=Object(IInput),
                  title=u'A list of media to caption',
                  required=True)

    subtitle_languages = List(value_type=Choice(vocabulary=SUBTITLE_LANGUAGE_VOCABULARY),
                              title=u'A list of language codes to request foreign language subtitles',
                              required=False)

    output_file_formats = List(value_type=Choice(vocabulary=OUTPUT_FILE_FORMAT_VOCABULARY),
                               title=u'A list of file formats the captions should be optimized for',
                               description=u'By default, we optimize for SubRip',
                               required=False)


class ICaptionOrderRequest(IOrderRequest):
    """
    An object providing information for placing a caption order
    """

    non_standard_tat_guarantee = Bool(title=u'Specify that normal turnaround time is not needed',
                                      description=u"""By default, normal turnaround time (false) is assumed.
                                      Note that this value is used as a guideline only.""",
                                      required=False)

    caption_options = Object(schema=ICaptionOptions,
                             title=u'Caption options for a caption order',
                             description=u"""Provides information on what needs to be captioned 
                             and specifies the desired captions output format""",
                             required=True)


class ICaptionOrder(ICaptionOrderRequest, ICaptionOrderDetails, IOrder):
    """
    A caption order
    """


class ITranscription(interface.Interface):
    """
    Transcription details for a transcription order
    including total length of the audio of media attachments for the order
    and additional services
    """

    total_length_seconds = Number(title=u'Total length of the audio (in seconds) of media attachments for an order',
                                  required=True)

    verbatim = Bool(title=u'The transcription is verbatim',
                    description=u"""If true, all filler words (i.e. umm, huh) are included in the transcription""",
                    required=True)

    timestamps = Bool(title=u'Timestamps are included in the transcription',
                      required=True)


class ITranscriptionOrderDetails(IOrderDetails):
    """
    The details of a transcription order
    """

    transcription = Object(schema=ITranscription,
                           title=u'Transcription details for the transcription order',
                           description=u"""Total length of the audio (in seconds) of media attachments for the order 
                           and additional services""",
                           required=True)


class ITranscriptionOrder(ITranscriptionOrderRequest, ITranscriptionOrderDetails, IOrder):
    """
    A transcription order
    """
