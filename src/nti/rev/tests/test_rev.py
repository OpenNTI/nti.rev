#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import unittest

import fudge

from hamcrest import assert_that
from hamcrest import calling
from hamcrest import is_
from hamcrest import is_not
from hamcrest import raises

from nti.rev import rev_client

from nti.rev.interfaces import RevAPIException

from nti.rev.model import Credentials
from nti.rev.model import Orders

from nti.rev.rev import RevClient

from nti.rev.tests import SharedConfiguringTestLayer

class TestRevClient(unittest.TestCase):

    def setUp(self):
        self.client = RevClient(BaseURL=str('https://rev_url/api/v1/'), credentials=Credentials(client_api_key='client_api_key', user_api_key='user_api_key'))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://rev_url/api/v1/'))
    
    # TODO: test more extensively?
    def test_operation_url_construction(self):
        url = self.client.url_for_operation('orders', params={'orderNumber': 'order_number'})
        assert_that(url, is_('https://rev_url/api/v1/orders?orderNumber=order_number'))
 
    # TODO: test more extensively?
    def test_order_url_construction(self):
        url = self.client._order_url('order_number')
        assert_that(url, is_('https://rev_url/api/v1/orders/order_number'))
 
    def test_orders_url_construction(self):
        # test with no parameters
        url = self.client._orders_url({})
        assert_that(url, is_('https://rev_url/api/v1/orders'))
         
        # test with one parameter
        url = self.client._orders_url({'ids': 'order_number'})
        assert_that(url, is_('https://rev_url/api/v1/orders?ids=order_number'))
         
        # test with multiple parameters
        # FIXME: Since python dictionary doesn't necessarily preserve order of keys,
        # url could be https://rev_url/api/v1/orders?page=0&pageSize=25 or https://rev_url/api/v1/orders?pageSize=25&page=0
        url = self.client._orders_url({'page': 0, 'pageSize': 25})
        assert_that(url, is_('https://rev_url/api/v1/orders?page=0&pageSize=25'))
         
        # test if parameter is None that it is not included in the url
        url = self.client._orders_url({'page': 0, 'ids': None})
        assert_that(url, is_('https://rev_url/api/v1/orders?page=0'))
 
    # TODO: test more extensively?
    def test_attachment_url_construction(self):
        url = self.client._attachment_url('attachment_id')
        assert_that(url, is_('https://rev_url/api/v1/attachments/attachment_id'))
 
#     # TODO: use mock objects
#     def test_get_order(self):
#         order = self.client.get_order('CP0927624606')
#         assert_that(order.order_number, is_('CP0927624606'))
 
    @fudge.patch('nti.rev.utils.NetSession', 'requests.Response')
    def test_get_orders(self, fake_session, fake_response):
        # create mock response
        (fake_response.has_attr(status_code=200)
                      .expects('json')
                      .returns(
                          {
                              'total_count': 2,
                              'results_per_page': 25,
                              'page': 0,
                              'orders': [
                                  {
                                      'order_number': 'TC432432',
                                      'price': 56,
                                      'status': 'Transcribing',
                                      'priority': 'Normal',
                                      'non_standard_tat_guarantee': True,
                                      'caption': {
                                          'total_length': 0,
                                          'total_length_seconds': 43
                                      },
                                      'comments': [],
                                      'attachments': []
                                  },
                                  {
                                      'order_number': 'CP0569871576',
                                      'client_ref': '6',
                                      'price': 1,
                                      'status': 'Complete',
                                      'priority': 'Normal',
                                      'non_standard_tat_guarantee': False,
                                      'caption': {
                                          'total_length': 0,
                                          'total_length_seconds': 43
                                      },
                                      'comments': [],
                                      'attachments': []
                                  }]
                          }))
         
        # create mock session
        # expect calling get_orders() with no arguments to call _orders_url() with default params
        (fake_session.expects('get')
                     .with_args(self.client._orders_url({'page':0, 'pageSize':25, 'ids':None, 'clientRef':None}))
                     .returns(fake_response))
        self.client.session = fake_session
         
        # (see above) test calling get_orders with no arguments uses default params
        orders = self.client.get_orders()
         
        # test Order object created
        assert_that(isinstance(orders, Orders), is_(True))
         
        # FIXME: Do I need to test that every Order attribute was assigned correctly?
        assert_that(orders.total_count, is_(2))
    
    @fudge.patch('nti.rev.utils.NetSession', 'requests.Response')
    def test_get_orders_exception(self, fake_session, fake_response):    
        # create mock response
        # expect calling json on a response with status code 400 Bad Request and no valid json in the response body will result in a Value Error
        (fake_response.has_attr(status_code=400)
                      .expects('json')
                      .raises(ValueError))
        
        # create mock session
        # expect making a request with both order_number and client_ref specified will result in a response with status code 400 Bad Request
        (fake_session.expects('get')
                     .with_args(self.client._orders_url({'page':0, 'pageSize':25, 'ids':'order_number', 'clientRef':'client_ref'}))
                     .returns(fake_response))
        self.client.session = fake_session
         
        # test exception raised when both order_number and client_ref are specified
        assert_that(calling(self.client.get_orders).with_args(order_number='order_number', client_ref="client_ref"),
                    raises(RevAPIException))

#     # TODO: use mock objects
#     def test_get_attachment(self):
#         attachment = self.client.get_attachment('nm1KN6ROAwAAAAAA')
#         assert_that(attachment.id, is_('nm1KN6ROAwAAAAAA'))

class TestCredentials(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_credentials(self):
        # verify the client_api_key and user_api_key in the configure.zcml
        # if it's 401, then they are invalid
        client = rev_client()
        url = client._orders_url({'ids': 'TC432432'})
        
        # make HTTP request
        result = client.session.get(url)
        # check status code to make sure not unauthorized
        assert_that(result.status_code, is_not(401))