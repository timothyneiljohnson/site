# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('signup_date', models.DateTimeField(blank=True, null=True)),
                ('rep_email', models.CharField(blank=True, max_length=31, null=True)),
                ('rep_first_name', models.CharField(blank=True, max_length=9, null=True)),
                ('rep_last_name', models.CharField(blank=True, max_length=12, null=True)),
                ('rep_zip_code', models.CharField(blank=True, max_length=12, null=True)),
                ('rep_phone', models.IntegerField(blank=True, null=True)),
                ('county', models.CharField(blank=True, max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('size', models.CharField(blank=True, max_length=21, null=True)),
                ('last_meeting', models.DateTimeField(blank=True, null=True)),
                ('types_of_organizing', models.TextField(blank=True, null=True)),
                ('mission_vision', models.TextField(blank=True, null=True)),
                ('issues', models.CharField(blank=True, max_length=257, null=True)),
                ('leadership_structure', models.TextField(blank=True, null=True)),
                ('constituency', models.TextField(blank=True, null=True)),
                ('leadership_positions', models.TextField(blank=True, null=True)),
                ('social_media', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
