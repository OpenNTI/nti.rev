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

from nti.rev.rev import RevClient

from nti.rev import rev_client

from nti.rev.tests import SharedConfiguringTestLayer

class TestRevClient(unittest.TestCase):

    def setUp(self):
        self.client = RevClient(BaseURL=str('https://api-sandbox.rev.com/api/v1/'))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://api-sandbox.rev.com/api/v1/'))
    
    def test_operation_construction(self):
        url = self.client.url_for_operation('orders', params={'orderNumber': 'TC432432'})
        assert_that(url, is_('https://api-sandbox.rev.com/api/v1/orders?orderNumber=TC432432'))
    
    # _entry_information_url > test_entry_information | _orders_url > test_orders
    #def test_orders(self):
        # TODO
    
    # TODO: fetch_entry_information > nowhere? | get_orders > somewhere
    # test default values
    # test errors/exceptions, like providing both orderNumber and referenceId

class TestCredentials(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_credentials(self):
        # verify the client_api_key and user_api_key in the configure.zcml
        # if it's 401, then they are invalid
        client = rev_client()
        url = client.BaseURL    # FIXME: use URL that requires authorization
        
        # TODO: make HTTP request
        result = client.session.get(url)
        # TODO: check status code to make sure not unauthorized
        assert_that(result.status_code, is_not(401))