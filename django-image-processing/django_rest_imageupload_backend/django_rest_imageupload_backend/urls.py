"""django_rest_imageupload_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings
from imageupload_frontend.views import operations, flip, thumbnail, resize, rotate

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/', include(('imageupload_rest.urls', 'api'), namespace='api')),
    re_path(r'^', include(('imageupload_frontend.urls', 'frontend'), namespace='frontend')),
    re_path(r'^operations/$', operations, name='operations'),
    re_path(r'^flip/$', flip, name='flip'),
    re_path(r'^thumbnail/$', thumbnail, name='thumbnail'),
    re_path(r'^resize/$', resize, name='resize'),
    re_path(r'^rotate/$', rotate, name='rotate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
