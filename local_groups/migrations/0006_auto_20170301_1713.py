# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 17:13
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('local_groups', '0005_auto_20170301_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='rep_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]
