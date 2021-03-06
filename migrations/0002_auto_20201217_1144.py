# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-17 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project1',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='project1',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='project1',
            name='age',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='project1',
            name='city',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='project1',
            name='state',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='project1',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
