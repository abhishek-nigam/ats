# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_info', '0004_auto_20170627_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='time_last_updated',
            field=models.DateField(auto_now_add=True),
        ),
    ]