from django.db import models

from authentication.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_correct = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Result(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result')
    result = models.IntegerField()

