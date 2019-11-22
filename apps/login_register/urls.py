from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^create$', views.create),
    url(r'^final_setup$', views.final_setup),
    url(r'^process_setup$', views.process_setup),
    url(r'^login_valid$', views.login_valid), 
    url(r'^logout$', views.logout),
]