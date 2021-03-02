from topit import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/magic$', views.magic_list),
    url(r'^api/magic/(?P<pk>[0-9]+)$', views.magic_detail),
    url(r'^api/magic/published$', views.magic_list_published)
]
