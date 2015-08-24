"""
Django settings for django-materialize-template project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

---
Updated to include configurations on environment variables.
It will fallback on development-only default values.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
from django.utils.translation import ugettext_lazy as _
from warnings import warn
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

allowed_environment_configurations = ['DEBUG', 'SECRET_KEY', 'ALLOWED_HOSTS',
                                      'DATABASE_URL', 'MEDIA_ROOT', 'STATIC_ROOT',
                                      'EMAIL_BACKEND']

unset_configurations = [variable for variable in allowed_environment_configurations
                        if variable not in os.environ]

if len(unset_configurations) >= 1:
    warn("Configurations %s not set. Using development default." %
         unset_configurations)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', '(gr3x=4wa%h22ae!#=df4$)1nrko6j7)%rj+equ51c6sqpkd-y')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

hosts = os.environ.get('ALLOWED_HOSTS', "")

ALLOWED_HOSTS = hosts.split()

STATIC_ROOT = os.environ.get('STATIC_ROOT', join(BASE_DIR, 'staticfiles'))

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', join(BASE_DIR, 'media'))

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {'default': dj_database_url.parse(
    os.environ.get('DATABASE_URL', 'sqlite:///%s/db.sqlite3' % BASE_DIR))}

if 'postgres' in DATABASES['default']['ENGINE']:
    DATABASES['default']['ENGINE'] = 'django_postgrespool'


EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# Application definition
INSTALLED_APPS = (
    'pipeline',
    'accounts',
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATIC_URL = '/static/'

STATICFILES_DIRS = [join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'


# CSS Files.
PIPELINE_CSS = {
    # Project libraries.
    'libraries': {
        'source_filenames': (
            'bower_components/materialize/dist/css/materialize.css',
        ),
        # Compress passed libraries and have
        # the output in`css/libs.min.css`.
        'output_filename': 'css/libs.min.css',
    }
    # ...
}
# JavaScript files.
PIPELINE_JS = {
    # Project JavaScript libraries.
    'libraries': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
            'bower_components/materialize/dist/js/materialize.js',
        ),
        # Compress all passed files into `js/libs.min.js`.
        'output_filename': 'js/libs.min.js',
    }
    # ...
}

LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Brazilian Portuguese')),
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
