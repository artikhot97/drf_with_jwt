# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-01-24 15:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210121_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmpolyee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=5)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empolyee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
