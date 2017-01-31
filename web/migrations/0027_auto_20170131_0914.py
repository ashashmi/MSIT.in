# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-31 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_delete_generalupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='category',
            field=models.CharField(choices=[('administration', 'Administration'), ('office', 'Office Staff'), ('accounts', 'Accounts'), ('library', 'Library Staff'), ('placement', 'Placement Staff'), ('teaching', 'Teaching Faculty')], default='teaching', max_length=30),
        ),
    ]
