# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compte',
            name='image',
        ),
    ]
