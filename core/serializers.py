from rest_framework import serializers
from .models import *


class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeopleModel
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
