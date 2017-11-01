#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from requests import Session

DEFAULT_REQUEST_TIMEOUT = 10 #pretty low for now

class NetSession(Session):

    timeout = DEFAULT_REQUEST_TIMEOUT

    def __init__(self, timeout=DEFAULT_REQUEST_TIMEOUT):
        super(NetSession, self).__init__()
        self.timeout = timeout

    def request(self, *args, **kwargs):
        if kwargs.get('timeout', None) is None:
            kwargs['timeout'] = self.timeout
        return super(NetSession, self).request(*args, **kwargs)

def make_session(url=None, credentials=None, timeout=DEFAULT_REQUEST_TIMEOUT):
    result = NetSession(timeout=timeout)
    if credentials:
        result.auth = (credentials.client_api_key, credentials.user_api_key)    # changed from credentials.username, credentials.password
    return result