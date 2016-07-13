# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from .settings import TAGS_MANAGER_NAME


# Because 're' module do not support \p{L} unicode class
# need to use simplistic regex with \w instead \p{L}. But such regexp
# also match digits like #123, #003 and so on.
# So it need to further filter out digit-only tags.
# See https://regex101.com/r/cK5oJ0/
HASHTAG_EXP = r'(?:^|_|[^\w&/]+)(?:#|＃)([\wÀ-ÖØ-öø-ÿ]+)'
HASHTAG_REGEX = re.compile(HASHTAG_EXP, re.UNICODE | re.IGNORECASE)


def parse_hashtags_from_text(text, to_lower_case=True):
    return (
        t.lower() if to_lower_case else t
        for t in HASHTAG_REGEX.findall(text)
        if not t.isdigit()
    )


def parse_hashtags(post, post_body):
    # All tags in lower case here
    tags = parse_hashtags_from_text(post_body)
    if tags:
        manager = getattr(post, TAGS_MANAGER_NAME)
        manager.add(*tags)
