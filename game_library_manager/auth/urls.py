from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import register


# create urlpatterns from router
urlpatterns = [
    path("register/", register),
]
