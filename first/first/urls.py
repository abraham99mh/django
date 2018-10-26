from django.conf.urls import include, url

from uno import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    url(r'^registro', views.registro),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
