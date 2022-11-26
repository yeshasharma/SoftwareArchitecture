#from django.conf.urls import url, include
from django.urls import re_path, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    re_path(r'^', include(router.urls))
]