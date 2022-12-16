from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from Account.models import User, ToDo
from Account.serializers import UserSerializer, ToDoSerializer

import datetime

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
        
    
class ToDoOperationsAPIView(APIView):
    """
    ToDO CRUD OPERATIONS
    """
    def get(self, request, *args, **kwargs):
        obj = ToDo.objects.all()
        srl_orj = ToDoSerializer(obj, many=True)
        return Response(srl_orj.data)


    def post(self, request, *args, **kwargs):
        input_data = request.data.copy()
        now = datetime.datetime.now()
        print(input_data)
        obj = ToDo(user_id = input_data["user_id"], title = input_data["title"], description = input_data["desc"], tags = input_data["tags"], datetime = now)
        obj.save()
        return Response("Todo list added!!")

    def patch(self, request, *args, **kwargs):
        input_data = request.data.copy()
        obj = ToDo.objects.get(to_id=input_data["todo_id"])
        updated_data ={}
        if "title" in input_data:
            updated_data["title"] = input_data["title"]
        if "description" in input_data:
            updated_data["description"] = input_data["desc"]
        if "tags" in input_data:
            updated_data["tags"] = input_data["tags"]
        if "is_completed" in input_data:
            updated_data["is_completed"] = input_data["is_completed"]
        if "is_important" in input_data:
            updated_data["is_important"] = input_data["is_important"]
            
        srl_obj = ToDoSerializer(obj, data = updated_data)
        if srl_obj.is_valid():
            srl_obj.save()
            return Response("Todo Updated successfully!!!")
        else:
            return Response(srl_obj.errors)
    
    


class ToDoviewerAPIView(APIView):
    """
    TO VIEW ToDO BASED ON USER_ID
    """

    def get(self, request, *args, **kwargs):
        input_data = request.query_params.get("user_id")
        obj = ToDo.objects.filter(user_id = input_data)
        srl_obj = ToDoSerializer(obj, many=True)
        return Response(srl_obj.data)