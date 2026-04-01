from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import refresh_key, register


# create urlpatterns from router
urlpatterns = [
    path("register", register),
    path("token", views.obtain_auth_token),
    path("refresh", refresh_key),
]
