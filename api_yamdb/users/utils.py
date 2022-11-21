from random import randrange

from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

MIN_CONFIRMATION_CODE = 10000
MAX_CONFIRMATION_CODE = 100000


def create_confirmation_code():
    return str(randrange(MIN_CONFIRMATION_CODE, MAX_CONFIRMATION_CODE))


def send_confirmation_code(user):
    send_mail(
        subject=f'Подтверждение авторизации пользователя {user.username}',
        message=(f'Добрый день, {user.username}! Для того, чтобы завершить '
                 'регистрацию Вам необходимо отправить запрос на адрес '
                 f'api/v1/auth/token/ с username: {user.username} и с '
                 f'кодом: {user.confirmation_code}'),
        from_email='admin.45cohort@yandex.ru',
        recipient_list=[user.email]
    )


def create_jwt_token(user):
    return str(RefreshToken.for_user(user).access_token)
