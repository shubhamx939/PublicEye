from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from Account.models import User
from Account.serializers import UserSerializer


# Create your views here.

class UserDetailAPIView(APIView):
    """
    CREATE, READ, UPDATE AND DELETE API
    """
    def get(self, request, *args, **kwargs):
        input_data = request.query_params.get("user_id")
        obj = User.objects.get(user_id = input_data)
        srl_obj = UserSerializer(instance=obj)
        return Response(srl_obj.data)


    def post(self, request, *args, **kwargs):
        input_data = request.data.copy()
        user_obj = User(fname=input_data["fname"],lname=input_data["lname"],email=input_data["email"],mobile=input_data["mobile"],gender=input_data["gender"])
        user_obj.save()
        return Response("User Saved Successfully!!!")


    def patch(self, requset, *args, **kwargs):
        input_data = requset.data.copy()
        obj = User.objects.get(user_id=input_data["user_id"])

        update_data = { "lname" : input_data["lname"]}
        srl_obj = UserSerializer(instance = obj, data=update_data)
        if srl_obj.is_valid():
            srl_obj.save()
            return Response(srl_obj.data)
        else:
            return Response(srl_obj.errors)
    
    def delete(self, request, *args, **kwargs):
        input_data = request.query_params.get("user_id")
        obj = User.objects.get(user_id=input_data)
        obj.delete()
        return Response("User Deleted Successfully!!!")
        