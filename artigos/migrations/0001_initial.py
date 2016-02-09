# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name=b'T\xc3\xadtulo')),
                ('url', models.SlugField(help_text=b'URL based in title', max_length=200, unique=True, verbose_name=b'URL')),
                ('pub_date', models.DateField(verbose_name=b'Data publica\xc3\xa7\xc3\xa3o')),
                ('content', models.TextField(verbose_name=b'Conteudo da p\xc3\xa1gina')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artigos.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='authors',
            field=models.ManyToManyField(to='artigos.Author'),
        ),
    ]