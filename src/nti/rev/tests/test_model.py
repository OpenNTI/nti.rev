#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import has_properties
from hamcrest import is_
from hamcrest import not_none

from nti.externalization import internalization

from nti.externalization.externalization import toExternalObject

import unittest

from nti.rev.model import ClientAPIKey
from nti.rev.model import UserAPIKey
from nti.rev.model import SourceFileUpload

from nti.rev.tests import SharedConfiguringTestLayer

class TestExternalization(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def _internalize(self, external, context=None):
        factory = internalization.find_factory_for(external)
        assert_that(factory, is_(not_none()))
        new_io = factory() if context is None else context
        internalization.update_from_external_object(new_io, external)
        return new_io

    def test_client_api_key(self):
        client_api_key = ClientAPIKey(client_api_key=u'qClt2chhujNEX6QXPHXmqzt9z3k')
        external = toExternalObject(client_api_key)
        assert_that(external, has_entries({'client_api_key': 'qClt2chhujNEX6QXPHXmqzt9z3k',
                                           'MimeType': 'application/vnd.nextthought.rev.clientapikey'}))

        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'client_api_key': 'qClt2chhujNEX6QXPHXmqzt9z3k'}))

    def test_user_api_key(self):
        user_api_key = UserAPIKey(user_api_key=u'AAAOiFQ21PgbaVUDAU1tYH2ZEV8=')
        external = toExternalObject(user_api_key)
        assert_that(external, has_entries({'user_api_key': 'AAAOiFQ21PgbaVUDAU1tYH2ZEV8=',
                                           'MimeType': 'application/vnd.nextthought.rev.userapikey'}))

        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'user_api_key': 'AAAOiFQ21PgbaVUDAU1tYH2ZEV8='}))

    def test_source_file_upload(self):
        source_file_upload = SourceFileUpload(content_type=u'video/mpeg',
                                              filename=u'video.mp4',
                                              url=str('http://www.server.com/file/987834'))
        external = toExternalObject(source_file_upload)
        assert_that(external, has_entries({'content_type': 'video/mpeg',
                                           'filename': 'video.mp4',
                                           'url': 'http://www.server.com/file/987834',
                                           'MimeType': 'application/vnd.nextthought.rev.sourcefileupload'}))
 
        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'content_type': 'video/mpeg',
                                           'filename': 'video.mp4',
                                           'url': 'http://www.server.com/file/987834'}))
