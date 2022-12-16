from rest_framework import serializers

from Account.models import User, ToDo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'fname',
            'lname',
            'email',
            'mobile',
            'gender'
        ]

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'