from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        password: str = validated_data.pop("password")

        # Create and save user
        user: User = User(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(password)
        user.save()

        # Generate authentification token
        token: Token = Token.objects.create(user=user)
        print(token)
        return user
