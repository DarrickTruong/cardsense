# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-24 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0007_auto_20191124_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall.Message'),
        ),
    ]
