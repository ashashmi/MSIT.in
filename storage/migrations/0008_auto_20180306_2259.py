# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-06 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_auto_20180306_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchrecord',
            name='isbn',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ISBN/ISSN'),
        ),
        migrations.AlterField(
            model_name='researchrecord',
            name='pages',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Page No'),
        ),
    ]
