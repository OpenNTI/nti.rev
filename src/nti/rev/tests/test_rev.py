#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import unittest

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
        self.client = RevClient(BaseURL=str('https://api-sandbox.rev.com/api/v1/'), credentials=Credentials(client_api_key='qClt2chhujNEX6QXPHXmqzt9z3k', user_api_key='AAAOiFQ21PgbaVUDAU1tYH2ZEV8='))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://api-sandbox.rev.com/api/v1/'))
    
    def test_operation_construction(self):
        url = self.client.url_for_operation('orders', params={'orderNumber': 'TC432432'})
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders?orderNumber=TC432432'))

    def test_order(self):
        url = self.client._order_url('TC432432')
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders/TC432432'))

    def test_orders(self):
        url = self.client._orders_url({'orderNumber': 'TC432432'})
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders?orderNumber=TC432432'))

    def test_get_order(self):
        order = self.client.get_order('CP0927624606')
        assert_that(order.order_number, is_('CP0927624606'))

    def test_get_orders(self):
        # test default values if no arguments specified
        orders = self.client.get_orders()
        assert_that(orders.page, is_(0))
        assert_that(orders.results_per_page, is_(25))
        
        # test arguments specified
        orders = self.client.get_orders(page=2, results_per_page=10)
        assert_that(orders.page, is_(2))
        assert_that(orders.results_per_page, is_(10))
        
        # test results_per_page set to default if argument specified is out of bounds
        orders = self.client.get_orders(results_per_page=4)
        assert_that(orders.results_per_page, is_(25))

        orders = self.client.get_orders(results_per_page=101)
        assert_that(orders.results_per_page, is_(25))

        # test only orders matching specified order_number are retrieved
        orders = self.client.get_orders(order_number='CP0927624606')
        for order in orders.orders:
            assert_that(order.order_number, is_('CP0927624606'))
        
        # test only orders matching specified client_ref are retrieved
        orders = self.client.get_orders(client_ref='myref1')
        for order in orders.orders:
            assert_that(order.client_ref, is_('myref1'))
        
        # test exception raised when both order_number and client_ref are specified
        assert_that(calling(self.client.get_orders).with_args(order_number='CP0927624606', client_ref="myref1"),
                    raises(RevAPIException))

        # test no orders found matching specified order_number or client_ref
        orders = self.client.get_orders(order_number=0)
        assert_that(orders.total_count, is_(0))
        assert_that(orders.orders, is_([]))
        
        orders = self.client.get_orders(client_ref='None')
        assert_that(orders.total_count, is_(0))
        assert_that(orders.orders, is_([]))

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