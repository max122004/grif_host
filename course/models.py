from django.db import models


class Level(models.IntegerChoices):
    low = 1, 'Лёгкий'
    medium = 2, 'Продвинутый'
    high = 3, 'Профильный'
    critical = 4, 'Специалитет'


class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cource/', default=1, null=True)

    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень', choices=Level.choices, default=2
    )


class Category(models.Model):
    name = models.CharField(max_length=200)
    course = models.ManyToManyField(Course, related_name='courses')