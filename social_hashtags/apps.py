from django.core.exceptions import ImproperlyConfigured
from django.apps import AppConfig, apps

from . import settings


class DjangoSocialHashtagsConfig(AppConfig):
    name = 'social_hashtags'
    verbose_name = 'Django Social Hashtags'

    def ready(self):
        # Set for each pluggable model django-taggit TaggableManager
        from taggit.managers import TaggableManager
        for app in settings.PLUGGABLE_APPS:
            try:
                model = apps.get_model(*app)
            except LookupError as e:
                raise ImproperlyConfigured(str(e))
            model.add_to_class(settings.TAGS_MANAGER_NAME,
                               TaggableManager(blank=True))