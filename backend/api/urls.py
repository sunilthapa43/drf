from rest_framework import routers
from django.urls import path, include
from . import views

#router = routers.SimpleRouter()
#router.register('data', views.api_home, basename='data')
#
urlpatterns = [
   path( '', views.api_home),
]