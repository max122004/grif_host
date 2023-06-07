from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from course.models import Course, Category
from course.serializer import CategoryListSerializer, CourseCreateSerializer


class CourseListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CourseCreateAPIVIew(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
# class CourseDetailAPIView(RetrieveAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseDetailSerializer
