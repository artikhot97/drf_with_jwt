# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-01-21 19:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manger', to=settings.AUTH_USER_MODEL),
        ),
    ]