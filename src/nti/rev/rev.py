#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import component
from zope import interface

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

from nti.rev.interfaces import ICredentials
from nti.rev.interfaces import IRevClient
from nti.rev.interfaces import IRevRoot

from nti.rev.utils import make_session

@interface.implementer(IRevClient)
class RevClient(SchemaConfigured):

    createDirectFieldProperties(IRevClient)

    session = None

    def __init__(self, BaseURL=None, credentials=None):
        self.BaseURL = BaseURL
        self.session = make_session(self.BaseURL, credentials=credentials)

#     def upload_source_file(self, source_file_upload):
        
#     def submit_transcription_order(self, transcription_order_request):
    
#     def submit_caption_order(self, caption_order_request):

#     def get_order(self, ordernum):

#     def get_orders(self, pagenum=1, pageSize=25, orderNumber=None, referenceId=None):

#     def cancel_order(self, ordernum):

#     def get_attachment(self, attachment_id):

#     def get_attachment_content(self, attachment_id, file_format):

@interface.implementer(IRevClient)
def rev_client_factory():
    base = component.getUtility(IRevRoot)
    creds = component.getUtility(ICredentials)
    
    logger.info('Registering Rev client with base %s', base.BaseURL)
    
    return RevClient(BaseURL=base.BaseURL, credentials=creds)