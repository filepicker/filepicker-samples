from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import app

urlpatterns = patterns(
    '',
    url(r'^', include(app.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
