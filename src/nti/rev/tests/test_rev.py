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

from nti.rev.rev import RevClient

class TestRevClient(unittest.TestCase):

    def setUp(self):
        self.client = RevClient(BaseURL=str('https://api-sandbox.rev.com/api/v1/'))

    def test_baseurl(self):
        assert_that(self.client.BaseURL, is_('https://api-sandbox.rev.com/api/v1/'))