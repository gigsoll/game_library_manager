from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def get_token(username: str) -> str:
    result: str = Token.objects.values_list("key", flat=True).get(
        user__username=username
    )
    return result


@api_view(["POST"])
def register(request):
    "Register user to api and generate token for them"
    serializer = UserSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        token = get_token(serializer.data["username"])
        return Response({"token": token})


@api_view(["POST"])
def refresh_key(request):
    user = authenticate(**request.data)

    if user is not None:
        t = Token.objects.get(user=user)
        t.delete()
        Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        return Response({"token": token.key}, 200)
    else:
        return Response(status=401)
