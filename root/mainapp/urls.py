from django.urls import path, include


from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', user, basename='user')

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('api/', include("rest_framework.urls")),
    path('login', login_view, name="login")
]