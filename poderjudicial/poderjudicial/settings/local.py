from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS= [BASE_DIR.child('static')]

import os
MEDIA_URL = '/EXPEDIENTES/'

MEDIA_ROOT= os.path.join(BASE_DIR, 'EXPEDIENTES')