from ast import Store
from urllib import response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from core.serializers import *
from core.models import *
import requests
import json
import http
from sms_ir import SmsIr
import ast


@api_view(["POST"])
@permission_classes([AllowAny])
def create_people(request):
    s_data = request.data
    data_save = {}
    data_serializers = PeopleSerializers(data=s_data)
    data_check = PeopleModel.objects.filter(
        phone_number=request.data["phone_number"]
    ).first()
    if data_check is not None:
        return Response("user is allow...", status=status.HTTP_208_ALREADY_REPORTED)
    else:
        if data_serializers.is_valid():
            account = data_serializers.save()
            data_save["phone_number"] = account.phone_number
            data_save["count"] = account.count
            data_save["is_sms"] = account.is_sms
            data_save["is_recive"] = account.is_recive
            data_save["sms_date"] = account.sms_date
            data_save["recive_date"] = account.recive_date
            data_save["recive_time"] = account.recive_time
            return Response(data_save, status=status.HTTP_201_CREATED)
        return Response(data_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_sms_people(request):
    etid_data = request.data
    edit_data_find_in_database = PeopleModel.objects.get(id=etid_data["id"])
    edit_data_find_in_database.is_sms = etid_data["is_sms"]
    phone = etid_data["phone_number"]
    message = etid_data["message"]
    sms_ir = SmsIr(
        "eakkbYygGNyC4BvGM5F1uIvvhQNeHpOyYfK7hNciF2dYn2C0eY4wWOtrddC6grL7",
        "300089931197",
    )
    sms_ir.send_sms(phone, message, "300089931197")
    sms_ir.report_latest_received(5)
    edit_data_find_in_database.save()
    return Response("form is update succesfully....", status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_sms_all_people(request):
    etid_data = request.data
    phone = etid_data["phone_number"]
    id = etid_data["id"]
    # list_phone = ast.literal_eval(phone)
    # list_id = ast.literal_eval(id)
    print(phone)
    print(id)
    message = etid_data["message"]
    sms_ir = SmsIr(
        "eakkbYygGNyC4BvGM5F1uIvvhQNeHpOyYfK7hNciF2dYn2C0eY4wWOtrddC6grL7",
        "300089931197",
    )
    sms_ir.send_bulk_sms(phone, message, "300089931197")
    for x in id:
        edit_data_find_in_database = PeopleModel.objects.get(id=x)
        edit_data_find_in_database.is_sms = True
        edit_data_find_in_database.save()
    return Response("form is update succesfully....", status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_recive_people(request):
    etid_data = request.data
    edit_data_find_in_database = PeopleModel.objects.get(id=etid_data["id"])
    edit_data_find_in_database.is_recive = etid_data["is_recive"]
    edit_data_find_in_database.save()
    return Response("form is update succesfully....", status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_people(request):
    data = PeopleModel.objects.all()
    return Response(PeopleSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_filter_people(request):
    data = PeopleModel.objects.filter(is_sms=False, is_recive=False)
    return Response(PeopleSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_sms_people(request):
    data = PeopleModel.objects.filter(is_sms=True, is_recive=False)
    return Response(PeopleSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_recive_people(request):
    data = PeopleModel.objects.filter(is_sms=True, is_recive=True)
    return Response(PeopleSerializers(data, many=True).data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    s_data = request.data
    data_save = {}
    data_serializers = UserSerializers(data=s_data)
    data_check = UserModel.objects.filter(
        phone_number=request.data["phone_number"]
    ).first()
    if data_check is not None:
        return Response("user is allow...", status=status.HTTP_208_ALREADY_REPORTED)
    else:
        if data_serializers.is_valid():
            account = data_serializers.save()
            data_save["phone_number"] = account.phone_number
            data_save["password"] = account.password
            data_save["is_active"] = account.is_active
            return Response(data_save, status=status.HTTP_201_CREATED)
        return Response(data_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    info = {}
    user = UserModel.objects.filter(
        phone_number=request.data["phone_number"], password=request.data["password"]
    ).first()
    if user.is_active == True:
        if user is not None:
            info["id"] = user.id
            info["is_active"] = user.is_active
            info["phone_number"] = user.phone_number
            info["password"] = user.password
            return Response(info, status=status.HTTP_200_OK)
        else:
            return Response(
                "The entered data is incorrect", status=status.HTTP_204_NO_CONTENT
            )
    return Response("user not active", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_user(request):
    user_data = UserModel.objects.all()
    return Response(
        UserSerializers(user_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def delete_user_by_id(request, id):
    user_data_for_delete = UserModel.objects.filter(id=id)
    user_data_for_delete.delete()
    return Response("user is delete...", status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_user(request):
    etid_data = request.data
    edit_data_find_in_database = UserModel.objects.get(id=etid_data["id"])
    edit_data_find_in_database.is_active = etid_data["is_active"]
    edit_data_find_in_database.save()
    return Response("form is update succesfully....", status=status.HTTP_200_OK)
