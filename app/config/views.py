# import mimetypes
# import os
# from django.conf import settings
# from django.http import FileResponse
#
#
# def serve_media(request, path):
#     # path에는 미디어 파일(User-uploaded files)의 경로가 주어짐
#     # 주어진 미디어파일의 경로를 settings.MEDIA_ROOT를 기준으로해서
#     # 해당 파일을 리턴해주는 view함수 작성
#
#
#     print('-')
#     print(path)
#     print('-')
#
#     # 방법 1 - 내 방법 <path>
#     # media_photo = os.path.join(settings.MEDIA_ROOT, 'photo')
#     # media_path = os.path.join(media_photo, path)
#
#     # 방법 2 - 수업시간 실습
#
#     media_path = os.path.join(settings.MEDIA_ROOT, path)
#     print(media_path)
#
#     content_type, encoding = mimetypes.guess_type(path)
#     # print(encoding)
#
#     return FileResponse(
#         open(media_path, 'rb'),
#         # content_type='image/jpeg'
#         content_type=content_type
#     )
