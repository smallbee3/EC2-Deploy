from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    '.amazonaws.com'
]

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
DATABASES = secrets['DATABASES']


WSGI_APPLICATION = 'config.wsgi.production.application'


# ## S3와 연결 ##
# # Media(User-uploaded files)를 위한 스토리지
# # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
#
# # Static files(collectstatic)를 위한 스토리지
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'config.storages.StaticStorage'
#
#
# MEDIAFILES_LOCATION = 'media'
# STATICFILES_LOCATION = 'static'
