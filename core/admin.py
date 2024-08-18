from django.contrib import admin
from .models import *

# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    fields = [
        "phone_number",
        "count",
        "is_sms",
        "is_recive",
        "is_reject",
        "sms_date",
        "recive_date",
        "recive_time",
    ]
    list_display = [
        "phone_number",
        "count",
        "is_sms",
        "is_recive",
        "is_reject",
    ]
    search_fields = ["phone_number"]


class UserAdmin(admin.ModelAdmin):
    fields = [
        "phone_number",
        "password",
        "is_active",
    ]
    list_display = ["phone_number"]
    search_fields = ["phone_number"]


admin.site.register(PeopleModel, PeopleAdmin)
admin.site.register(UserModel, UserAdmin)
