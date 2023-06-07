from django.shortcuts import render
from rest_framework.generics import ListAPIView

from news.models import News
from news.serializer import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
