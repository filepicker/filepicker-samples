from django.conf.urls import patterns, url
from app.views import (
    save_image,
    images_list,
    index,
    image_view,
    image_delete
)


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^upload/$', save_image, name='save_image'),
    url(r'^list/$', images_list, name='images_list'),
    url(r'^list/(?P<fid>\d+)/$', image_view, name='image_view'),
    url(r'^list/(?P<fid>\d+)/delete/$', image_delete, name='image_delete')
)