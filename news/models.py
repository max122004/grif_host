from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='news/', default=1, null=True)
    created = models.DateTimeField(auto_now_add=True)
