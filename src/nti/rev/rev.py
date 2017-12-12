#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import urlparse
from urllib import urlencode

from requests.exceptions import ConnectionError

from zope import component
from zope import interface

from nti.externalization.internalization import update_from_external_object

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

from nti.rev.interfaces import ICredentials
from nti.rev.interfaces import IRevClient
from nti.rev.interfaces import IRevRoot

from nti.rev.interfaces import RevAPIException
from nti.rev.interfaces import RevUnreachableException

from nti.rev.model import Attachment
from nti.rev.model import Order
from nti.rev.model import Orders

from nti.rev.utils import make_session

def _transform_json_results(response, expected_response=200):
    """
    Inspects the response and returns the json body of the response if
    the response was successful. Raises an exception if the response was
    unsuccessful.
    """
    
    # if response did not execute successfully
    if expected_response is not None and expected_response != response.status_code:
        # try to get error code and message from response body
        error_code = None
        message = None
        try:
            body = response.json()[0]
            error_code = body.get(u'code')
            message = body.get(u'message')
        except:
            logger.exception('Unable to get description of error from body.')
            pass

        raise RevAPIException(message, error_code=error_code, status_code=response.status_code)

    try:
        body = response.json()
    except ValueError:
        logger.exception('No JSON object could be decoded')
        raise RevAPIException('No JSON object could be decoded')
    
    return body

@interface.implementer(IRevClient)
class RevClient(SchemaConfigured):

    createDirectFieldProperties(IRevClient)

    session = None

    def __init__(self, BaseURL=None, credentials=None):
        self.BaseURL = BaseURL
        self.session = make_session(self.BaseURL, credentials=credentials)

    def url_for_operation(self, entity_type, params={}):
        """
        Constructs a URL for the desired entity and params
        """

        base = self.BaseURL 
        # append the operation-specific component to the base URL
        joined = urlparse.urljoin(base, entity_type)

        # parse URL into 6 components: scheme, netloc, path, params, query, fragment
        components = list(urlparse.urlparse(joined))

        # create dictionary by parsing query string (components[4]) into name, value pairs
        query = dict(urlparse.parse_qsl(components[4]))

        # if a parameter value is None, remove the parameter entry from the params dictionary
        for key in params.keys():
            if params.get(key) is None:
                del params[key]

        # add the params dictionary into the query dictionary
        query.update(params)

        # convert query dictionary to percent-encoded string of
        # key=value pairs separated by '&' characters
        components[4] = urlencode(query)

        # concatenate URL components back into URL
        return urlparse.urlunparse(components)

    def _order_url(self, order_number):
        return (self.url_for_operation('orders') + '/' + order_number)

    def _orders_url(self, params={}):
        return self.url_for_operation('orders', params=params)
    
    def _attachment_url(self, attachment_id):
        return (self.url_for_operation('attachments') + '/' + attachment_id)

    def get_order(self, order_number):
        url = self._order_url(order_number)

        logger.info('Getting order with order number %s', order_number)
        logger.debug('Using Rev API %s', url)

        try:
            response = self.session.get(url)
        except ConnectionError:
            logger.exception('Connection error communicating with %s', url)
            raise RevUnreachableException('Unable to connect to Rev system.')

        logger.info('Completed request for order with order number %s', order_number)

        result = _transform_json_results(response)
        logger.debug('Received response from Rev %s', result)

        # Create and return Order object providing IOrder interface from the response JSON
        return Order(**result)

    def get_orders(self, page=0, results_per_page=25, order_number=None, client_ref=None):
        url = self._orders_url(params={'page': page,
                                       'pageSize': results_per_page,
                                       'ids': order_number,
                                       'clientRef': client_ref})

        logger.info('Getting page number %s of size %s for orders with order number %s or reference ID %s', page, results_per_page, order_number, client_ref)
        logger.debug('Using Rev API %s', url)

        try:
            response = self.session.get(url)
        except ConnectionError:
            logger.exception('Connection error communicating with %s', url)
            raise RevUnreachableException('Unable to connect to Rev system.')

        logger.info('Completed request for page number %s of size %s for orders with order number %s or reference ID %s', page, results_per_page, order_number, client_ref)

        result = _transform_json_results(response)
        logger.debug('Received response from Rev %s', result)
        
        # update_from_external_object
        orders = Orders()
        
        # Add MimeType to each order
        for order in result['orders']:
            order['MimeType'] = 'application/vnd.nextthought.rev.order'
            
            # Add MimeType to order caption
            if 'caption' in order:
                order['caption']['MimeType'] = 'application/vnd.nextthought.rev.caption'

#         from IPython.core.debugger import Tracer;Tracer()()

        return update_from_external_object(orders, result)

    def get_attachment(self, attachment_id):
        url = self._attachment_url(attachment_id)

        logger.info('Getting attachment with attachment id %s', attachment_id)
        logger.debug('Using Rev API %s', url)

        try:
            response = self.session.get(url)
        except ConnectionError:
            logger.exception('Connection error communicating with %s', url)
            raise RevUnreachableException('Unable to connect to Rev system.')

        logger.info('Completed request for attachment with attachment id %s', attachment_id)

        result = _transform_json_results(response)
        logger.debug('Received response from Rev %s', result)

        # Create and return Attachment object providing IAttachment interface from the response JSON
        return Attachment(**result)

#     def upload_source_file(self, source_file_upload):
        
#     def submit_transcription_order(self, transcription_order_request):
    
#     def submit_caption_order(self, caption_order_request):

#     def cancel_order(self, ordernum):

#     def get_attachment_content(self, attachment_id, file_format):

@interface.implementer(IRevClient)
def rev_client_factory():
    base = component.getUtility(IRevRoot)
    creds = component.getUtility(ICredentials)
    
    logger.info('Registering Rev client with base %s', base.BaseURL)
    
    return RevClient(BaseURL=base.BaseURL, credentials=creds)