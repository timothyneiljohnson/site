# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateendorsementpage',
            name='signup_tagline',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
