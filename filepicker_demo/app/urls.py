from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^list/$', files_list_view, name='list'),
    url(r'^list/(?P<fid>\d+)/$', file_detailed_view, name='detailed'),
    url(r'^upload/$', file_upload_view, name='upload'),
    url(r'^list/(?P<fid>\d+)/delete/$', file_delete_view, name='delete'),
)
