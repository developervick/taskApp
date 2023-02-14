from django.shortcuts import render, HttpResponse

from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.

def index(request):
    return HttpResponse("this is index")

class entryview(viewsets.ModelViewSet):
    queryset = entry.objects.all()
    serializer_class = main_ser

def send_otp(requests):
    return None