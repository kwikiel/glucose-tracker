import os

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'akr2icmg1n8%z^3fe3c+)5d0(t^cy-2_25rrl35a7@!scna^1#'

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT=587
EMAIL_USE_TLS=True

ADMINS = (
    ('Local Admin', 'admin@glucosetracker.net'),
)

MANAGERS = ADMINS

CONTACTS = {
    'support_email': 'support@glucosetracker.net',
    'admin_email': 'admin@glucosetracker.net',
    'info_email': 'info@glucosetracker.net',
}

# For 'subscribers' app
SEND_SUBSCRIBERS_EMAIL_CONFIRMATION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'glucosetracker',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += ('debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += \
    ('debug_toolbar.middleware.DebugToolbarMiddleware', )

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS':False,
    'SHOW_TEMPLATE_CONTEXT':True,
    'HIDE_DJANGO_SQL':False,
}