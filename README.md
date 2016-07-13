Django Social Hashtags App
==========================
This app allow you to parse hashtags from text and adds its to any model instance. For managing tags app uses django-taggit model manager.

Intallation
-----------
```bash
# pip install git+https://github.com/ramusus/django-social-hashtags
```
Add into `settings.py` lines:
```python
    INSTALLED_APPS = [
        ...
        'taggit',
        'social_hashtags.apps.DjangoSocialHashtagsConfig',
    ]
    
    # Optional django-social-hashtags settings (here default values)
    # Pluggable apps and models for django-taggit manager
    SOCIAL_HASHTAGS_PLUGGABLE_APPS = (  # (('app_label', 'app_model'), ... )
        ('vkonakte_wall', 'Post'),
        ('facebook_posts', 'Post'),
        ('odnoklassniki_discussions', 'Discussion'),
        ('instagram_api', 'Media'),
        ('twitter_api', 'Status'),
    )
    # django-taggit manager name
    SOCIAL_HASHTAGS_TAGS_MANAGER_NAME = 'hashtags'
```

Usage examples
--------------
For tags manager API see [django-taggit docs](https://django-taggit.readthedocs.io/en/latest/)

```python
from social_hashtags.api import parse_hashtags
from social_hashtags.api import parse_hashtags_from_text
from vkontakte_wall.models import Post

post = Post.objects.create()
parse_hashtags(post, u'text #HashTag1 #хеш_тег')
post.hashtags.names()
# [u'hashtag1', u'хеш_тег']

tags = parse_hashtags_from_text(u'text #HashTag1 #хеш_тег', to_lower_case=False)
list(tags)
[u'HashTag1', u'хеш_тег']
```

Tests
-----
To run the django-social-hashtags tests:

* Download the [source from GitHub](https://github.com/ramusus/django-social-hashtags) or your fork.
* Install tox
    ```bash
    # pip install tox
    ```
* Run tox
    ```bash
    $ tox
    ```
This will run all the tests on all supported combinations of Django/Python.


Licensing
---------
This library uses the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).
Please see the library's individual files for more information.


Release notes
-------------
Version 0.0.1
* Initial release