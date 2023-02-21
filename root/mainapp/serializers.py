from rest_framework import serializers

from .models import *

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']

class task_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = tasks_list
        fields = ['task', 'status']
    
        