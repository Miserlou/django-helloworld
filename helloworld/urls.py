from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^json_example/$', 'hello.views.json_example', name='json_example'),
    url(r'^post_echo/$', 'hello.views.post_echo', name='post_echo'),
    url(r'^unicode_401/$', 'hello.views.unicode_401', name='unicode_401'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
]
