from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^wall/(?P<user_id>\d+)$', views.thewall),
    url(r'^edit_contact/$', views.edit_contact),
    url(r'^process_edit_contact$', views.process_edit_contact),
    url(r'^write_message/(?P<user_id>\d+)$', views.write_message),
    url(r'^convert_lead$', views.convert_lead),
    url(r'^process_message/(?P<user_id>\d+)$', views.process_message),
    url(r'^comment/(?P<message_id>\d+)$', views.comment),
    url(r'^pin_message/(?P<message_id>\d+)$', views.pin_message),
    url(r'^unpin_message/(?P<message_id>\d+)$', views.unpin_message),
    url(r'^write_review/(?P<user_id>\d+)$', views.write_review),
    url(r'^process_review/(?P<user_id>\d+)$', views.process_review),
    url(r'^destroy_review$', views.destroy_review),
    url(r'^process_event$', views.process_event),
    url(r'^update_profile_pic$', views.update_profile_pic),
    url(r'^edit_event/(?P<event_id>\d+)$', views.edit_event),
    url(r'^process_edit_event/(?P<event_id>\d+)$', views.process_edit_event),
    url(r'^update_event_pic/(?P<event_id>\d+)$', views.update_event_pic),
    url(r'^destroy_event/(?P<event_id>\d+)$', views.destroy_event),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)