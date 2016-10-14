from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_articulo),
        url(r'^post/new/$', views.postear_nuevo, name='postear_nuevo'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_post, name='editar_post'),
]
