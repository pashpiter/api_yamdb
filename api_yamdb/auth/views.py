from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from reviews.models import User
from .serializers import SignupSerializer, GetTokenSerializer
from .utils import (
    create_confirmation_code,
    send_confirmation_code,
    create_jwt_token
)


class APISignup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        try:
            user, flag = User.objects.get_or_create(
                username=username,
                email=email
            )
        except Exception as error:
            raise ValidationError(
                (f'Ошибка создания нового пользователя {error}. '
                 'Данный username или email уже существует')
            )
        user.confirmation_code = create_confirmation_code()
        user.save()
        send_confirmation_code(user)
        return Response(serializer.validated_data, status=HTTP_200_OK)


class APIGetToken(APIView):
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(User, username=username)
        if confirmation_code != user.confirmation_code:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response({"token": create_jwt_token(user)})
