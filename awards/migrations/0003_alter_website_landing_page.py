# Generated by Django 3.2.9 on 2021-12-16 19:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20211215_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='landing_page',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Landing page image'),
        ),
    ]