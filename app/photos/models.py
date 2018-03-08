import os
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage as storage

User = get_user_model


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)

    # Photo모델이 삭제되는 시점의 signal을 이용해서
    # 인스턴스가 삭제될 때 file필드의 파일도 삭제하도록 구현


# 1) post_delete
@receiver(post_delete, sender=Photo)
def remove_file_from_s3(sender, instance, using, **kwargs):
    print(f'sender: {sender}')
    print(f'instance: {instance}')
    print(f'using: {using}')
    print(f'**kwargs: {kwargs}')
    instance.file.delete(save=False)
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    # if instance.file:
    #     if os.path.isfile(storage.open(instance.file.path)):
    #         os.remove(storage.open(instance.file.path))


# 2) django-cleanup


# # 3) boto3
# import boto
# from boto.s3.key import Key
# from django.conf import settings
#
# def s3_delete(id):
#     s3conn = boto.connect_s3(settings.AWS_ACCESS_KEY,
#                              settings.AWS_SECRET_ACCESS_KEY)
#     bucket = s3conn.get_bucket(settings.S3_BUCKET)
#
#     k = Key(bucket)
#     k.key = str(id)
#     k.delete()
