# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercontacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
