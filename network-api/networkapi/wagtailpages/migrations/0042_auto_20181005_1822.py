# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-05 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0041_auto_20181005_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypage',
            name='author',
            field=models.CharField(blank=True, max_length=50, verbose_name='Byline'),
        ),
        migrations.AlterField(
            model_name='storypage',
            name='date',
            field=models.DateField(help_text='For display on page. This does not affect when the page goes live', verbose_name='Post date'),
        ),
    ]
