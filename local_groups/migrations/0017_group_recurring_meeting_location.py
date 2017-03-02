# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 20:01
from __future__ import unicode_literals

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('local_groups', '0016_auto_20170302_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='recurring_meeting_location',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
    ]
