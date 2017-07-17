# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Room', models.CharField(max_length=50)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('duration', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]
