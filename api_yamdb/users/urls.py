from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, APISignup, APIGetToken

v1_router = DefaultRouter()
v1_router.register(
    'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/users/signup/', APISignup.as_view(), name='signup'),
    path('v1/users/token/', APIGetToken.as_view(), name='get_token')
]
