from django.contrib import admin
from django.urls import path, include

from task import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('list/<int:category_id>/', views.QuestionListAPIView.as_view())
]