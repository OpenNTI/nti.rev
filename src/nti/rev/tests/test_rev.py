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
from hamcrest import is_
from hamcrest import is_not

from nti.rev.model import Credentials

from nti.rev.rev import RevClient

from nti.rev import rev_client

from nti.rev.tests import SharedConfiguringTestLayer

class TestRevClient(unittest.TestCase):

    def setUp(self):
        self.client = RevClient(BaseURL=str('https://api-sandbox.rev.com/api/v1/'), credentials=Credentials(client_api_key='qClt2chhujNEX6QXPHXmqzt9z3k', user_api_key='AAAOiFQ21PgbaVUDAU1tYH2ZEV8='))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://api-sandbox.rev.com/api/v1/'))
    
    def test_operation_construction(self):
        url = self.client.url_for_operation('orders', params={'orderNumber': 'TC432432'})
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders?orderNumber=TC432432'))
    
    def test_orders(self):
        url = self.client._orders_url({'orderNumber': 'TC432432'})
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders?orderNumber=TC432432'))

    def test_get_orders(self):
        result = self.client.get_orders()
        # test default values
        
        # test orders retrieved meet specified parameters
        
        # test only orders matching specified orderNumber are retrieved
        
        # test only orders matching specified referenceId are retrieved
        
        # test exception raised when both orderNumber and referenceId are specified
        
        # what is the functionality if no orders are found matching specified orderNumber or referenceId?

class TestCredentials(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_credentials(self):
        # verify the client_api_key and user_api_key in the configure.zcml
        # if it's 401, then they are invalid
        client = rev_client()
        url = client._orders_url({'orderNumber': 'TC432432'})
        
        # make HTTP request
        result = client.session.get(url)
        # check status code to make sure not unauthorized
        assert_that(result.status_code, is_not(401))