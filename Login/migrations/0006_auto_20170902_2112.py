# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-02 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_auto_20170902_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mbno',
        ),
    ]
