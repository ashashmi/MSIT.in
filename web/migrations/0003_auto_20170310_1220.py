# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import functools
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170309_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marquee',
            name='content',
        ),
        migrations.AddField(
            model_name='marquee',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(web.models.wrapper, *(), **{b'field': 'title', b'folder': 'marquee'})),
        ),
        migrations.AddField(
            model_name='marquee',
            name='link',
            field=models.CharField(blank=True, help_text='Link to redirect to', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='marquee',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='marquee',
            name='title',
            field=models.CharField(help_text='Text to show in the Marquee', max_length=50, verbose_name='Link Title'),
        ),
    ]
