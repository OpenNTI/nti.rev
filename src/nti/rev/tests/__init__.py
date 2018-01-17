#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

import unittest

from z3c.baseregistry.baseregistry import BaseComponents

import zope.testing.cleanup

from zope.component.hooks import setHooks
from zope.component.hooks import site

from zope.interface.adapter import AdapterRegistry
from zope.interface.adapter import BaseAdapterRegistry

from zope.interface.registry import Components

from nti.appserver.policies.sites import BASEADULT

from nti.site.transient import TrivialSite

from nti.testing.layers import GCLayerMixin
from nti.testing.layers import ZopeComponentLayer
from nti.testing.layers import ConfiguringLayerMixin

from persistent.persistence import Persistent

class SharedConfiguringTestLayer(ZopeComponentLayer,
                                 GCLayerMixin,
                                 ConfiguringLayerMixin):

    set_up_packages = ('nti.rev',)

    @classmethod
    def setUp(cls):
        setHooks()
        cls.setUpPackages()

    @classmethod
    def tearDown(cls):
        cls.tearDownPackages()
        zope.testing.cleanup.cleanUp()

    @classmethod
    def testSetUp(cls, unused_test=None):
        setHooks()

    @classmethod
    def testTearDown(cls):
        pass

class IsolatedAdapterRegistry(AdapterRegistry):

    def _setBases(self, bases):
        # Avoid using _addSubregistry to avoid leaving references around
        # (and because it might not exist!)
        BaseAdapterRegistry._setBases(self, bases)

class IsolatedComponents(Persistent, Components):

    def _init_registries(self):
        self.adapters = IsolatedAdapterRegistry()
        self.utilities = IsolatedAdapterRegistry()

    @property
    def __parent__(self):
        # So that IConnection(site_manager) can work.
        return self.__bases__[0]

_REV_SANDBOX_API_SITE = BaseComponents(BASEADULT, name='test.nti.rev', bases=(BASEADULT,))

class RevTestCase(unittest.TestCase):

    def testsite(self, site_manager=None):
        return site(TrivialSite(site_manager or _REV_SANDBOX_API_SITE))