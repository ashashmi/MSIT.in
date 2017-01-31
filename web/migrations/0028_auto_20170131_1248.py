# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-31 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_auto_20170131_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='branch',
            field=models.CharField(blank=True, choices=[('1', 'CSE'), ('2', 'IT'), ('3', 'ECE'), ('4', 'EEE'), ('5', 'Applied Sciences')], help_text='Branch Name', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='semester',
            field=models.CharField(blank=True, choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(blank=True, choices=[(1, 'CSE'), (2, 'IT'), (3, 'ECE'), (4, 'EEE'), (5, 'Applied Science')], max_length=100, null=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='semester',
            field=models.CharField(blank=True, choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='branch',
            field=models.CharField(blank=True, choices=[('1', 'CSE'), ('2', 'IT'), ('3', 'ECE'), ('4', 'EEE'), ('5', 'Applied Sciences')], help_text='Branch Name', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='semester',
            field=models.CharField(blank=True, choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], max_length=1, null=True),
        ),
    ]
