from django.test import SimpleTestCase
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps

from taggit.managers import _TaggableManager

from social_hashtags import settings
from social_hashtags.tests.models import Post

from .utils import override_settings


class DjangoSocialHashtagsConfigTestCase(SimpleTestCase):
    def test_if_tags_manager_in_app_model(self):
        self.assertTrue(hasattr(Post, settings.TAGS_MANAGER_NAME))
        self.assertTrue(isinstance(
            getattr(Post, settings.TAGS_MANAGER_NAME), _TaggableManager))

    def test_if_appconfig_raises_improperlyconfigured(self):
        with override_settings(PLUGGABLE_APPS=(('bad_app', 'bad_model'), )):
            self.assertRaises(ImproperlyConfigured,
                              apps.app_configs['social_hashtags'].ready)