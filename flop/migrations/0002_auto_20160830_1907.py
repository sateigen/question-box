# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 00:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='rated_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='rated_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='flop.Tag'),
        ),
    ]
