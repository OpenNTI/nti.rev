#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import zope.i18nmessageid
MessageFactory = zope.i18nmessageid.MessageFactory('nti.rev')

from zope import component

from nti.rev.interfaces import IRevClient

def rev_client():
    return component.getUtility(IRevClient)