from zope import interface

from nti.schema.field import Dict
from nti.schema.field import List
from nti.schema.field import Number
from nti.schema.field import Object
from nti.schema.field import HTTPURL
from nti.schema.field import TextLine

# class IHttpRequest(interface.Interface):
#     """
# 
#     """
# 
#     method = TextLine(title=u'The HTTP method', required=True)
# 
#     url = HTTPURL(title=u'The url', required=True)
# 
#     request_params = Dict(title=u'A dictionary of key-value parameters', required=False)
# 
#     request_headers = Dict(title=u'A dictionary of key-value headers', required=False)
# 
#     request_body
# 
#     response
# 
#     response_headers
# 
#     response_body
# 
# class IPostInputsRequest(IHttpRequest):
#     
# class IPostOrderRequest(IHttpRequest):
# 
# class IPostTranscriptOrderRequest(IPostOrderRequest):
#     
# class IPostCaptionOrderRequest(IPostOrderRequest):
# 
# class IGetOrderRequest(IHttpRequest):
# 
# class IGetOrdersRequest(IHttpRequest):
# 
# class IPostCancelOrderRequest(IHttpRequest):
# 
# class IGetAttachmentRequest(IHttpRequest):
# 
# class IGetAttachmentContentRequest(IHttpRequest):

#-------------------------------------------------
class IInputs(interface.Interface):
    """
    """

    inputs = List(title=u'A list of inputs', required=True)

class IInput(interface.Interface):
    """
    Describes a media source file to be retrieved, uploaded, and used in an order.
    """

    # If not specified, Rev will try to determine the content type from the server response
    content_type = TextLine(title=u'The content type of the media to be retrieved', required=False)

    # If not specified, Rev will try to determine the filename from the url
    filename = TextLine(title=u'The filename for the media', required=False)

    # URL must be publicly accessible.
    # HTTP URLs are ok as long as the site in question has a valid certificate.
    # FIXME: fields that provide url and uri validation
    url = TextLine(title=u'The URL where the media can be retrieved', required=True)

    uri = TextLine(title=u'A URI identifying the newly uploaded media', required=True)

#TODO: Input2

class IOrders(interface.Interface):
    """
    """
    # FIXME: value_type of object interface Object(IOrder)
    orders = List(title=u'A list of orders', required=True);

class IOrder(interface.Interface):
    """
    """

    client_ref = TextLine(title=u'A reference number for the order meaningful to the client', required=False)

    # Enables receiving notifications about the order status
    notification = Object(INotification, required=False)

    #----------------------------
    order_number = TextLine(title=u'Rev assigned order number', required=False)

    # TODO: determine units
    price = Number(title=u'Total cost of the order', required=False)

    # FIXME: Status of the order
    # FIXME: Choice
    # TODO: vocabulary of possible choices?
    status

    # Total length of the audio (in seconds) of media attachments for the order
    # and additional services
    transcription = Object(ITranscription, required = False)

class ITranscriptionOrder(IOrder):
    """
    """

    # Provides information on what needs to be transcribed
    # and allows for any transcsription options to be set
    transcription_options = Object(ITranscriptionOptions, required=True)

class ITranscriptionOptions(interface.Interface):
    """
    """

    # Must have at least one element
    inputs = List(title=u'A list of media to transcribe', required=True)

    # FIXME: Optional, should we transcribe the provided files verbatim?
    # FIXME: Boolean, if true, all filler words (i.e. umm, huh) will be included
    verbatim

    # FIXME: Optional, should we include timestamps?
    # FIXME: Boolean
    timestamps

class ICaptionOrder(IOrder):
    """
    """

    # FIXME: Optional, specify that normal turnaround time is not needed.
    # By default, normal turnaround time (false) is assumed.
    # Note that this value is used as a guideline only.
    # FIXME: Boolean
    non_standard_tat_guarantee

    # Provides information on what needs to be captioned
    # and specifies the desired captions output format
    caption_options = Object(ICaptionOptions, required=True)

class ICaptionOptions(interface.Interface):
    """
    """

    # Must have at least one element
    inputs = List(title=u'A list of media to caption', required=True)

    # FIXME: Optional, language codes to request foreign language subtitles.
    # FIXME: Choice
    # es, it, etc.
    subtitle_languages

    # FIXME: Optional, what file formats should the captions be optimized for.
    # By default, we optimize for SubRip
    # FIXME: Choice
    # SubRip, Scc, Mcc, Ttml, QTtext, Transcript, WebVtt,
    # Dfxp, CheetahCap, Stl, AvidDs, FacebookSubRip
    output_file_formats

class INotification(interface.Interface):
    """
    """

    # Updates will be posted to this URL
    url = TextLine(title=u'The url for notifications', required=True)

    # FIXME: Optional, specifies which notifications are sent
    # FIXME: Choice
    # If "Detailed", then a notification is sent whenever the order is in a new status of has a new comment.
    # If "FinalOnly" (the default), notification is sent only when the order is complete.
    level

class IAttachments(interface.Interface):
    """
    """

    attachments = List(title=u'A list of attachments')

class IAttachment(interface.Interface):
    """
    """

    #FIXME: Choice
    # media, transcript, caption
    kind

    name = TextLine(title=u'Filename for the attachment')

    id = TextLine(title=u'ID for the attachment')

    links = Object(ILinks)

    speakers = Object(ISpeakers)

    monologues = Object(IMonologues)

class ILinks(interface.Interface):
    """
    """

    links = List(title=u'A list of links')

class ILink(interface.Interface):
    """
    Link with URL of the resource for getting attachment content
    """

    rel = TextLine()

    href = TextLine()

class ISpeakers(interface.Interface):
    """
    """

    speakers = List(title=u'A list of speakers', required=True)

class ISpeaker(interface.Interface):
    """
    """

    id = Number(title=u'The ID of the speaker')

    name = TextField(title=u'The name of the speaker')

class IMonologues(interface.Interface):
    """
    """

    monologues = List(title=u'A list of monologues')

class IMonologue(interface.Interface):
    """
    """

    id = Number(title=u'The ID of the monologue')

    # Same as declared in ISpeaker
    speaker = Number(title=u'The ID of the speaker')

    # Same as declared in ISpeaker
    speaker_name = TextLine(title=u'The name of the speaker')

    elements = Object(IElements)

class IElements(interface.Interface):
    """
    Elements of a monologue.
    """

    elements = List(title=u'A list of elements')

class IElement(interface.Interface):
    """
    Each element of a monologue is either text (transcribed speech)
    or a tag (an annotation), such as inaudible or crosstalk.
    """

    # FIXME: Choice
    # text, tag
    type

    # FIXME
    # For text elements, value contains the text
    # For tag elements, value contains the annotation type
    value

    """
    Timestamp format is hh:mm:sss,fff,
    where fff represents milliseconds

    Text elements may or may not contain a timestamp.
    Tag elements require a timestamp.
    """
    timestamp = TextLine(title=u'The timestamp')
