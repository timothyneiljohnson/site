# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_groups', '0010_auto_20170301_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='mission_vision',
            new_name='description',
        ),
    ]
