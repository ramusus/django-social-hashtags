from django.conf import settings


_PLUGGABLE_APPS = (  # (('app_label', 'app_model'), ... )
    ('vkonakte_wall', 'Post'),
    ('facebook_posts', 'Post'),
    ('odnoklassniki_discussions', 'Discussion'),
    ('instagram_api', 'Media'),
    ('twitter_api', 'Status'),
)


PLUGGABLE_APPS = getattr(settings, 'SOCIAL_HASHTAGS_PLUGGABLE_APPS',
                         _PLUGGABLE_APPS)

TAGS_MANAGER_NAME = getattr(settings, 'SOCIAL_HASHTAGS_TAGS_MANAGER_NAME',
                            'hashtags')