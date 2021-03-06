# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailpages', '0023_auto_20180515_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('URL', models.URLField(help_text='The fully qualified URL that this page should map to.')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
