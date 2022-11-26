from django.urls import re_path, include
from django.views.generic.base import RedirectView
from imageupload_frontend.views import operations

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    re_path(r'^operations/$', operations, name='operations'),
]



















































































































































































































































































































































































































































































































































































































































































































































































