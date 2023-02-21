from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, serializers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions

from .models import *
from .serializers import *
from .forms import *

# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            pass

    return render(request, 'mainapp/login.html', {'login_form': login_form})



def signup_view(request):

    if request.method == 'POST':
        pass

    return render(request, "mainapp/signup.html", {'signup_form': sighnup_form })



def index(request):
    return render(request, 'mainapp/index.html')

# API views
#@api_view(['GET', 'POST'])
#def user(request):
#    
#        queryset = User.objects.all()
#        serialized = user_serializer(queryset, many=True)
#        return Response(serialized.data)

    

class user(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = user_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = user_serializer(user)
        return Response(serializer.data)
