from rest_framework import serializers

from Account.models import User

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