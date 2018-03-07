from .base import *
# from config.settings import base

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())
DATABASES = secrets['DATABASES']
