SECRET_KEY = 'FAKE_SECRET_KEY'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_nose',
    'taggit',
    'social_hashtags.tests',
    'social_hashtags.apps.DjangoSocialHashtagsConfig',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SOCIAL_HASHTAGS_PLUGGABLE_APPS = (
    ('tests', 'Post'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=social_hashtags',
    '--cover-inclusive',
    '--verbosity=1',
]