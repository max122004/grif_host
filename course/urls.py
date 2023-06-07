from django.contrib import admin
from django.urls import path, include

from course import views

urlpatterns = [
    path('list/', views.CourseListAPIView.as_view()),
    path('create/', views.CourseCreateAPIVIew.as_view())
    # path('<int:pk>/', views.CourseDetailAPIView.as_views_view())
]