from django.conf.urls import url
from .views import SensEmailsView, success

urlpatterns = [
    url(r'^$', SensEmailsView.as_view(), name='index'),
    url(r'^success', success, name='success'),
    # url(r'^image_load/$', image_load, name='image_load'),
]
