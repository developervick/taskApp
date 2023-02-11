from django.urls import path, include

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'entry', entryview)

urlpatterns = [
    path('main/', index, name="index"),
    path('', include(router.urls)),
]