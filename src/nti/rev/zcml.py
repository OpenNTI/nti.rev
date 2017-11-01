#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from functools import partial

from zope import interface

from zope.component.zcml import utility

from zope.configuration import fields

from nti.schema.field import HTTPURL

from nti.rev.interfaces import ICredentials
from nti.rev.interfaces import IRevRoot

from nti.rev.model import Credentials
from nti.rev.model import RevRoot

class IRegisterCredentials(interface.Interface):
    client_api_key = fields.TextLine(title="client API key", required=True)
    user_api_key = fields.TextLine(title="user API key", required=True)

class IRegisterRevEndpoint(interface.Interface):
    base = HTTPURL(title="The Base URL", required=True)

def registerRevEndpoint(_context, base):
    factory = partial(RevRoot, BaseURL=base)
    utility(_context, provides=IRevRoot, factory=factory)

def registerCredentials(_context, client_api_key, user_api_key):
    factory = partial(Credentials, client_api_key=client_api_key, user_api_key=user_api_key)
    utility(_context, provides=ICredentials, factory=factory)