# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190319_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
    ]
