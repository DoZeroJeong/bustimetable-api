from .base import *

HOST = get_secret(setting="DATABASE_HOST")
NAME = get_secret(setting="DATABASE_NAME")
PORT = get_secret(setting="DATABASE_PORT")
PASSWORD = get_secret(setting="DATABASE_PASSWORD")

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgre',
        'USER': NAME,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT
    }
}
