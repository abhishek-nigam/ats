# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='force_employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('experience', models.PositiveSmallIntegerField(default=0)),
                ('license_no', models.PositiveIntegerField()),
                ('ph_no', models.BigIntegerField()),
                ('in_service', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='security_forces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('license_no', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='force_employee',
            name='force',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.security_forces'),
        ),
    ]
