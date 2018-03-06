"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from config.views import serve_media


urlpatterns = [
    path('admin/', admin.site.urls),

    # *이렇게 <path>안에 /가 포함된 형태로는 사용할 수 없다.
    # path('media/<path>', serve_media),

    path('media/photo/<path>/', serve_media),
    # path('media/photo/<str:path>/', serve_media),
    # re_path(r'media/(?P<path>.*)/', serve_media),
]

# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT,
# )


# 잠깐 말씀드렸었는데 장고안에서 경로를 처리할 때는 유알엘 모듈에 의한 패턴에 의해서 어디로 갈지를 정하잖아요.
# 미디어 슬래시로 오는것은 특별히 처리. 뷰에서 처리되는게 아니라 그 경로에 있는 파일을 가져오겠다. 일반적ㅇ로 장고가 하는게 아니에요.
# 개발에서 그런것까지 하는게 아닌데. 그 런 뷰를 가져오는거에요.
# 뷰가 스태틱이 하는일이죠.
