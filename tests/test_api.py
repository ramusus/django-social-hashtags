# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, TestCase

from social_hashtags.api import (
    parse_hashtags_from_text, parse_hashtags
)
from social_hashtags.tests.models import Post
from social_hashtags.settings import TAGS_MANAGER_NAME


text_with_hashtags = """
Hashtags
#hashtag　text
＃hashtag
text　#hashtag
text #1tag
text.#hashtag
text #hashtag
text #hashtag!
text #hashtag1 #hashtag2
text #hash_tagüäö
text #hash0tag
text #hash_tag

Hashtags non-ACSII
#хэш_тег
#中英字典
#الأبجدية

Not hashtags
text #1234
&#nbsp;
text#hashtag
"""


class ApiParseHashtagsFromTextTestCase(SimpleTestCase):
    def test_if_correct_parse_hashtags_from_text(self):
        self.assertEqual(
            list(parse_hashtags_from_text(text_with_hashtags)),
            ['hashtag', 'hashtag', 'hashtag', '1tag', 'hashtag', 'hashtag',
             'hashtag', 'hashtag1', 'hashtag2', 'hash_tagüäö', 'hash0tag',
             'hash_tag', 'хэш_тег', '中英字典', 'الأبجدية']
        )


class ApiParseHashtagsTestCase(TestCase):
    def test_if_saves_hashtags(self):
        post = Post.objects.create(message='Hello')
        parse_hashtags(post, '#hashtag #хэш_тэг')
        post = Post.objects.get(message='Hello')
        hashtag_manager = getattr(post, TAGS_MANAGER_NAME)
        self.assertIn('hashtag', hashtag_manager.names())
        self.assertIn('хэш_тэг', hashtag_manager.names())
