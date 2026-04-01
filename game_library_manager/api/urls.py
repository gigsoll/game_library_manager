from django.urls import include, path

# Combine urls from different apps in API
urlpatterns = [
    path("auth/", include("auth.urls")),
]
