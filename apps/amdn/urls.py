from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.home),
    url(r'^amadon$', views.home),
    url(r'^amadon/buy$', views.buy),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^clear$', views.clear)
]