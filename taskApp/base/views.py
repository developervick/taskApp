from django.shortcuts import render
from django.http import request, HttpResponse
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

# Create your views here.
def index(request):
    return HttpResponse("index")

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

