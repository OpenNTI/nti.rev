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

import datetime
import unittest

from nti.rev.model import ClientAPIKey
from nti.rev.model import UserAPIKey
from nti.rev.model import SourceFileUpload
from nti.rev.model import SourceFileInput
from nti.rev.model import Comment
from nti.rev.model import Notification
from nti.rev.model import OrderRequest
from nti.rev.model import Link
from nti.rev.model import Links

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

#     # TODO: Test this? Only consists of ClientAPIKey and UserAPIKey
#     def test_authorization(self):

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

#     # TODO: Do I need to test this? Input doesn't have any fields
#     def test_input(self)

    # FIXME: How to set audio_length_seconds to Number schema type?
    def test_source_file_input(self):
        source_file_input = SourceFileInput(audio_length_seconds=60,
                                            uri=str('urn:rev:inputmedia:467432fds'))
        external = toExternalObject(source_file_input)
        assert_that(external, has_entries({'audio_length_seconds': 60,
                                           'uri': 'urn:rev:inputmedia:467432fds',
                                           'MimeType': 'application/vnd.nextthought.rev.sourcefileinput'}))
 
        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'audio_length_seconds': 60,
                                           'uri': 'urn:rev:inputmedia:467432fds'}))

#     def test_comment(self):
#         comment = Comment(by=u'John S.',
#                           timestamp=datetime.datetime(year=2003, month=04, day=05, hour=12, minute=20, second=30, microsecond=123),
#                           text=u'Please do it quickly')
#         external = toExternalObject(comment)
#         assert_that(external, has_entries({'by': 'John S.',
#                                            'timestamp': '2003-04-05T12:20:30.123',
#                                            'text': 'Please do it quickly',
#                                            'MimeType': 'application/vnd.nextthought.rev.comment'}))

    def test_notification(self):
        notification = Notification(url=str('http://www.clientsite.com/orderupdate'),
                                    level=u'Detailed')
        external = toExternalObject(notification)
        assert_that(external, has_entries({'url': 'http://www.clientsite.com/orderupdate',
                                           'level': 'Detailed',
                                           'MimeType': 'application/vnd.nextthought.rev.notification'}))

        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'url': 'http://www.clientsite.com/orderupdate',
                                           'level': 'Detailed'}))

    # FIXME: How to test when entries contain other entries, like order_request has notification
    def test_order_request(self):
        order_request = OrderRequest(client_ref=u'XB432423',
                                     notification=Notification(url=str('http://www.clientsite.com/orderupdate'), level=u'Detailed'))
        external = toExternalObject(order_request)
        assert_that(external, has_entries({'client_ref': 'XB432423',
                                           'notification': {u'MimeType': 'application/vnd.nextthought.rev.notification', 'url': 'http://www.clientsite.com/orderupdate', u'Class': 'Notification', 'level': u'Detailed'},
                                           'MimeType': 'application/vnd.nextthought.rev.orderrequest'}))

    def test_link(self):
        link = Link(rel=u'content',
                    href=u'https://www.rev.com/api/v1/attachments/1C4AA')
        external = toExternalObject(link)
        assert_that(external, has_entries({'rel': 'content',
                                           'href': 'https://www.rev.com/api/v1/attachments/1C4AA',
                                           'MimeType': 'application/vnd.nextthought.rev.link'}))

        new_io = self._internalize(external)
        assert_that(new_io, has_properties({'rel': 'content',
                                           'href': 'https://www.rev.com/api/v1/attachments/1C4AA'}))

#     # FIXME: No 'links' key?
#     def test_links(self):
#         link = Link(rel=u'content',
#                     href=u'https://www.rev.com/api/v1/attachments/1C4AA')
#         links = Links(links=[link])
#         external = toExternalObject(links)
#         assert_that(external, has_entries({'links': {'link': {'rel': 'content', 'href': 'https://www.rev.com/api/v1/attachments/1C4AA'}},
#                                                      'MimeType': 'application/vnd.nextthought.rev.links'}))
