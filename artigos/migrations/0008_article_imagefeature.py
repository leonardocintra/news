# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 15:00
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0007_remove_article_featureimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imageFeature',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagem'),
        ),
    ]
