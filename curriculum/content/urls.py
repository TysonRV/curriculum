from django.conf.urls import include, url
from django.contrib import admin

from curriculum.content.views import IndexView

admin.autodiscover()

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]

include(urlpatterns)
