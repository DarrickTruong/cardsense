# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-19 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0009_auto_20191124_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_messaged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='login_register.User'),
        ),
    ]