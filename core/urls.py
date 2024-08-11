from django.urls import path
from core import views

urlpatterns = [
    path("create_people", views.create_people),
    path("edit_sms_people", views.edit_sms_people),
    path("edit_recive_people", views.edit_recive_people),
    path("get_all_people", views.get_all_people),
    path("get_sms_people", views.get_sms_people),
    path("get_recive_people", views.get_recive_people),
    path("get_filter_people", views.get_filter_people),
    ###################################################
    path("create_user", views.create_user),
    path("login_user", views.login_user),
    path("get_all_user", views.get_all_user),
    path("edit_user", views.edit_user),
    path("delete_user_by_id/<int:id>", views.delete_user_by_id),
]
