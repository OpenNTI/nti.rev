#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import interface

from nti.externalization.persistence import NoPickle

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

from nti.rev.interfaces import IClientAPIKey
from nti.rev.interfaces import IUserAPIKey
from nti.rev.interfaces import ICredentials
from nti.rev.interfaces import IRevRoot
from nti.rev.interfaces import ISourceFileUpload
from nti.rev.interfaces import IInput
from nti.rev.interfaces import ISourceFileInput
from nti.rev.interfaces import IExternalLinkInput
from nti.rev.interfaces import ISpeaker
from nti.rev.interfaces import ISpeakers
from nti.rev.interfaces import IMonologueElement
from nti.rev.interfaces import IMonologueElements
from nti.rev.interfaces import IMonologue
from nti.rev.interfaces import IMonologues
from nti.rev.interfaces import IComment
from nti.rev.interfaces import INotification
from nti.rev.interfaces import ILink
from nti.rev.interfaces import ILinks
from nti.rev.interfaces import IAttachment
from nti.rev.interfaces import IAttachments
from nti.rev.interfaces import IAttachmentContent
from nti.rev.interfaces import IOrderRequest
from nti.rev.interfaces import IOrderDetails
from nti.rev.interfaces import IOrder
from nti.rev.interfaces import IOrders
from nti.rev.interfaces import ITranscriptionOptions
from nti.rev.interfaces import ITranscriptionOrderRequest
from nti.rev.interfaces import ICaption
from nti.rev.interfaces import ICaptionOrderDetails
from nti.rev.interfaces import ICaptionOptions
from nti.rev.interfaces import ICaptionOrderRequest
from nti.rev.interfaces import ICaptionOrder
from nti.rev.interfaces import ITranscription
from nti.rev.interfaces import ITranscriptionOrderDetails
from nti.rev.interfaces import ITranscriptionOrder

@NoPickle
@interface.implementer(IClientAPIKey)
class ClientAPIKey(SchemaConfigured):

    createDirectFieldProperties(IClientAPIKey)

    mimeType = mime_type = 'application/vnd.nextthought.rev.clientapikey'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IUserAPIKey)
class UserAPIKey(SchemaConfigured):

    createDirectFieldProperties(IUserAPIKey)

    mimeType = mime_type = 'application/vnd.nextthought.rev.userapikey'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICredentials)
class Credentials(SchemaConfigured):

    createDirectFieldProperties(ICredentials)

    mimeType = mime_type = 'application/vnd.nextthought.rev.credentials'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IRevRoot)
class RevRoot(SchemaConfigured):
    createDirectFieldProperties(IRevRoot)

@NoPickle
@interface.implementer(ISourceFileUpload)
class SourceFileUpload(SchemaConfigured):

    createDirectFieldProperties(ISourceFileUpload)

    mimeType = mime_type = 'application/vnd.nextthought.rev.sourcefileupload'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IInput)
class Input(SchemaConfigured):

    createDirectFieldProperties(IInput)

    mimeType = mime_type = 'application/vnd.nextthought.rev.input'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISourceFileInput)
class SourceFileInput(SchemaConfigured):

    createDirectFieldProperties(ISourceFileInput)

    mimeType = mime_type = 'application/vnd.nextthought.rev.sourcefileinput'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IExternalLinkInput)
class ExternalLinkInput(SchemaConfigured):

    createDirectFieldProperties(IExternalLinkInput)

    mimeType = mime_type = 'application/vnd.nextthought.rev.externallinkinput'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISpeaker)
class Speaker(SchemaConfigured):

    createDirectFieldProperties(ISpeaker)

    mimeType = mime_type = 'application/vnd.nextthought.rev.speaker'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISpeakers)
class Speakers(SchemaConfigured):

    createDirectFieldProperties(ISpeakers)

    mimeType = mime_type = 'application/vnd.nextthought.rev.speakers'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologueElement)
class MonologueElement(SchemaConfigured):

    createDirectFieldProperties(IMonologueElement)

    mimeType = mime_type = 'application/vnd.nextthought.rev.monologueelement'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologueElements)
class MonologueElements(SchemaConfigured):

    createDirectFieldProperties(IMonologueElements)

    mimeType = mime_type = 'application/vnd.nextthought.rev.monologueelements'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologue)
class Monologue(SchemaConfigured):

    createDirectFieldProperties(IMonologue)

    mimeType = mime_type = 'application/vnd.nextthought.rev.monologue'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologues)
class Monologues(SchemaConfigured):

    createDirectFieldProperties(IMonologues)

    mimeType = mime_type = 'application/vnd.nextthought.rev.monologues'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IComment)
class Comment(SchemaConfigured):

    createDirectFieldProperties(IComment)

    mimeType = mime_type = 'application/vnd.nextthought.rev.comment'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(INotification)
class Notification(SchemaConfigured):

    createDirectFieldProperties(INotification)

    mimeType = mime_type = 'application/vnd.nextthought.rev.notification'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ILink)
class Link(SchemaConfigured):

    createDirectFieldProperties(ILink)

    mimeType = mime_type = 'application/vnd.nextthought.rev.link'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ILinks)
class Links(SchemaConfigured):

    createDirectFieldProperties(ILinks)

    mimeType = mime_type = 'application/vnd.nextthought.rev.links'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachment)
class Attachment(SchemaConfigured):

    createDirectFieldProperties(IAttachment)

    mimeType = mime_type = 'application/vnd.nextthought.rev.attachment'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachments)
class Attachments(SchemaConfigured):

    createDirectFieldProperties(IAttachments)

    mimeType = mime_type = 'application/vnd.nextthought.rev.attachments'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachmentContent)
class AttachmentContent(SchemaConfigured):

    createDirectFieldProperties(IAttachmentContent)

    mimeType = mime_type = 'application/vnd.nextthought.rev.attachmentcontent'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrderRequest)
class OrderRequest(SchemaConfigured):

    createDirectFieldProperties(IOrderRequest)

    mimeType = mime_type = 'application/vnd.nextthought.rev.orderrequest'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrderDetails)
class OrderDetails(SchemaConfigured):

    createDirectFieldProperties(IOrderDetails)

    mimeType = mime_type = 'application/vnd.nextthought.rev.orderdetails'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrder)
class Order(SchemaConfigured):

    createDirectFieldProperties(IOrder)

    mimeType = mime_type = 'application/vnd.nextthought.rev.order'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrders)
class Orders(SchemaConfigured):

    createDirectFieldProperties(IOrders)

    mimeType = mime_type = 'application/vnd.nextthought.rev.orders'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOptions)
class TranscriptionOptions(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOptions)

    mimeType = mime_type = 'application/vnd.nextthought.rev.transcriptionoptions'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrderRequest)
class TranscriptionOrderRequest(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrderRequest)

    mimeType = mime_type = 'application/vnd.nextthought.rev.transcriptionorderrequest'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaption)
class Caption(SchemaConfigured):

    createDirectFieldProperties(ICaption)

    mimeType = mime_type = 'application/vnd.nextthought.rev.caption'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrderDetails)
class CaptionOrderDetails(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrderDetails)

    mimeType = mime_type = 'application/vnd.nextthought.rev.captionorderdetails'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOptions)
class CaptionOptions(SchemaConfigured):

    createDirectFieldProperties(ICaptionOptions)

    mimeType = mime_type = 'application/vnd.nextthought.rev.captionoptions'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrderRequest)
class CaptionOrderRequest(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrderRequest)

    mimeType = mime_type = 'application/vnd.nextthought.rev.captionorderrequest'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrder)
class CaptionOrder(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrder)

    mimeType = mime_type = 'application/vnd.nextthought.rev.captionorder'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscription)
class Transcription(SchemaConfigured):

    createDirectFieldProperties(ITranscription)

    mimeType = mime_type = 'application/vnd.nextthought.rev.transcription'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrderDetails)
class TranscriptionOrderDetails(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrderDetails)

    mimeType = mime_type = 'application/vnd.nextthought.rev.transcriptionorderdetails'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrder)
class TranscriptionOrder(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrder)

    mimeType = mime_type = 'application/vnd.nextthought.rev.transcriptionorder'

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)
