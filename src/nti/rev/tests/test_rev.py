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

from nti.rev.rev import RevClient

from nti.rev.tests import SharedConfiguringTestLayer

class TestRevClient(unittest.TestCase):

    def setUp(self):
        self.client = RevClient(BaseURL=str('https://rev_url/api/v1/'), credentials=Credentials(client_api_key='client_api_key', user_api_key='user_api_key'))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://rev_url/api/v1/'))
    
    def test_operation_construction(self):
        url = self.client.url_for_operation('orders', params={'orderNumber': 'order_number'})
        assert_that(url, is_('https://rev_url/api/v1/orders?orderNumber=order_number'))

    def test_order(self):
        url = self.client._order_url('order_number')
        assert_that(url, is_('https://rev_url/api/v1/orders/order_number'))

    def test_orders(self):
        url = self.client._orders_url({'orderNumber': 'order_number'})
        assert_that(url, is_('https://rev_url/api/v1/orders?orderNumber=order_number'))

    def test_attachment(self):
        url = self.client._attachment_url('attachment_id')
        assert_that(url, is_('https://rev_url/api/v1/attachments/attachment_id'))

    # TODO: use mock object
#     def test_get_order(self):
#         order = self.client.get_order('CP0927624606')
#         assert_that(order.order_number, is_('CP0927624606'))

    @fudge.patch('nti.rev.utils.NetSession', 'requests.Response')
    def test_get_orders(self, fake_session, fake_response):

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

        (fake_session.expects('get')
                     .with_args(self.client._orders_url({'page':0, 'pageSize':25}))
                     .returns(fake_response))
        self.client.session = fake_session
        
        orders = self.client.get_orders()
        
        # TODO: really testing building url, move some of these tests to test_orders
        # test default values if no arguments specified
        assert_that(orders.page, is_(0))
        assert_that(orders.results_per_page, is_(25))
        
#         # test arguments specified
#         orders = self.client.get_orders(page=2, results_per_page=10)
#         assert_that(orders.page, is_(2))
#         assert_that(orders.results_per_page, is_(10))
#         
#         # test results_per_page set to default if argument specified is out of bounds
#         orders = self.client.get_orders(results_per_page=4)
#         assert_that(orders.results_per_page, is_(25))
# 
#         orders = self.client.get_orders(results_per_page=101)
#         assert_that(orders.results_per_page, is_(25))
# 
#         # test only orders matching specified order_number are retrieved
#         orders = self.client.get_orders(order_number='CP0927624606')
#         for order in orders.orders:
#             assert_that(order.order_number, is_('CP0927624606'))
#         
#         # test only orders matching specified client_ref are retrieved
#         orders = self.client.get_orders(client_ref='myref1')
#         for order in orders.orders:
#             assert_that(order.client_ref, is_('myref1'))
#         
#         # test exception raised when both order_number and client_ref are specified
#         assert_that(calling(self.client.get_orders).with_args(order_number='CP0927624606', client_ref="myref1"),
#                     raises(RevAPIException))
# 
#         # test no orders found matching specified order_number or client_ref
#         orders = self.client.get_orders(order_number=0)
#         assert_that(orders.total_count, is_(0))
#         assert_that(orders.orders, is_([]))
#         
#         orders = self.client.get_orders(client_ref='None')
#         assert_that(orders.total_count, is_(0))
#         assert_that(orders.orders, is_([]))

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