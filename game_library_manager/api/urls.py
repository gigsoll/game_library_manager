from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, GameViwSet

# Combine urls from different apps in API

# Create router to handle viesets
router = DefaultRouter()
router.register(r"games", GameViwSet, basename="game")
router.register(r"genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("", include(router.urls)),
]
