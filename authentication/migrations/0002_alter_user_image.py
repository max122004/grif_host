# Generated by Django 4.2.1 on 2023-05-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, null=True, upload_to='logos/'),
        ),
    ]