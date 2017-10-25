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

