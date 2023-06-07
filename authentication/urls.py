from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateAPIView, Logout, UserListAPIView, UserAPIView, CustomAuthToken

urlpatterns = [
    path('register/', UserCreateAPIView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('profile/<int:pk>/', UserAPIView.as_view()),
]