from rest_framework import serializers

from .models import *

class main_ser(serializers.ModelSerializer):
    
    class Meta:
        model = entry
        fields = ('num', 'name')