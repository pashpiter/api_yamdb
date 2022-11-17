from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from reviews.models import User, CHOICES_ROLE


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Использовать имя "me" в качестве username запрещено.'
            )
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                (f'Данный username ({value}) уже существует в базе данных. '
                 'Выберите другой')
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                (f'Данный email ({value}) уже существует в базе данных. '
                 'Выберите другой')
            )
        return value


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=(UnicodeUsernameValidator,)
    )
    email = serializers.EmailField(max_length=254, required=True)
    role = serializers.ChoiceField(choices=CHOICES_ROLE)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role'
                  )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                (f'Данный username ({value}) уже существует в базе данных. '
                 'Выберите другой')
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                (f'Данный email ({value}) уже существует в базе данных. '
                 'Выберите другой')
            )
        return value


class MeUserSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)
