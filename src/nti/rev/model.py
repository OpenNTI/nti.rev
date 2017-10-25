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
from nti.rev.interfaces import IAuthorization
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

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IUserAPIKey)
class UserAPIKey(SchemaConfigured):

    createDirectFieldProperties(IUserAPIKey)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAuthorization)
class Authorization(SchemaConfigured):

    createDirectFieldProperties(IAuthorization)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISourceFileUpload)
class SourceFileUpload(SchemaConfigured):

    createDirectFieldProperties(ISourceFileUpload)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IInput)
class Input(SchemaConfigured):

    createDirectFieldProperties(IInput)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISourceFileInput)
class SourceFileInput(SchemaConfigured):

    createDirectFieldProperties(ISourceFileInput)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IExternalLinkInput)
class ExternalLinkInput(SchemaConfigured):

    createDirectFieldProperties(IExternalLinkInput)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISpeaker)
class Speaker(SchemaConfigured):

    createDirectFieldProperties(ISpeaker)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ISpeakers)
class Speakers(SchemaConfigured):

    createDirectFieldProperties(ISpeakers)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologueElement)
class MonologueElement(SchemaConfigured):

    createDirectFieldProperties(IMonologueElement)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologueElements)
class MonologueElements(SchemaConfigured):

    createDirectFieldProperties(IMonologueElements)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologue)
class Monologue(SchemaConfigured):

    createDirectFieldProperties(IMonologue)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IMonologues)
class Monologues(SchemaConfigured):

    createDirectFieldProperties(IMonologues)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IComment)
class Comment(SchemaConfigured):

    createDirectFieldProperties(IComment)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(INotification)
class Notification(SchemaConfigured):

    createDirectFieldProperties(INotification)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ILink)
class Link(SchemaConfigured):

    createDirectFieldProperties(ILink)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ILinks)
class Links(SchemaConfigured):

    createDirectFieldProperties(ILinks)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachment)
class Attachment(SchemaConfigured):

    createDirectFieldProperties(IAttachment)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachments)
class Attachments(SchemaConfigured):

    createDirectFieldProperties(IAttachments)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IAttachmentContent)
class AttachmentContent(SchemaConfigured):

    createDirectFieldProperties(IAttachmentContent)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrderRequest)
class OrderRequest(SchemaConfigured):

    createDirectFieldProperties(IOrderRequest)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrderDetails)
class OrderDetails(SchemaConfigured):

    createDirectFieldProperties(IOrderDetails)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrder)
class Order(SchemaConfigured):

    createDirectFieldProperties(IOrder)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(IOrders)
class Orders(SchemaConfigured):

    createDirectFieldProperties(IOrders)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOptions)
class TranscriptionOptions(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOptions)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrderRequest)
class TranscriptionOrderRequest(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrderRequest)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaption)
class Caption(SchemaConfigured):

    createDirectFieldProperties(ICaption)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrderDetails)
class CaptionOrderDetails(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrderDetails)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOptions)
class CaptionOptions(SchemaConfigured):

    createDirectFieldProperties(ICaptionOptions)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrderRequest)
class CaptionOrderRequest(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrderRequest)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ICaptionOrder)
class CaptionOrder(SchemaConfigured):

    createDirectFieldProperties(ICaptionOrder)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscription)
class Transcription(SchemaConfigured):

    createDirectFieldProperties(ITranscription)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrderDetails)
class TranscriptionOrderDetails(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrderDetails)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)

@NoPickle
@interface.implementer(ITranscriptionOrder)
class TranscriptionOrder(SchemaConfigured):

    createDirectFieldProperties(ITranscriptionOrder)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)
