# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-20 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_event_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
