from .base import *
# from config.settings import base

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASE']