# Generated by Django 3.2.9 on 2022-01-09 21:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='content',
            field=models.ManyToManyField(blank=True, related_name='content', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='website',
            name='design',
            field=models.ManyToManyField(blank=True, related_name='design', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='website',
            name='usability',
            field=models.ManyToManyField(blank=True, related_name='usability', to=settings.AUTH_USER_MODEL),
        ),
    ]