from django.db.models import F
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task.models import Category, Result, Question
from task.serializer import CategorySerializer, QuestionSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Question.objects.filter(category_id=category_id)


