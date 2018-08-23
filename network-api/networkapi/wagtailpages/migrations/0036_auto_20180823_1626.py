# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-23 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0001_squashed_0007_nullify_homepage'),
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailpages', '0035_auto_20180815_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTA4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('header', models.TextField(blank=True)),
                ('subhead', wagtail.core.fields.RichTextField(blank=True)),
                ('commitment', models.CharField(blank=True, help_text='Amount of time required (eg: "30 min commitment")', max_length=256)),
                ('buttonTitle', models.CharField(blank=True, max_length=250, verbose_name='Button Text')),
                ('buttonURL', models.TextField(blank=True, verbose_name='Button URL')),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cta_hero', to='wagtailimages.Image', verbose_name='Hero Image')),
            ],
            options={
                'verbose_name': 'cta',
                'verbose_name_plural': 'ctas',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipateHighlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('commitment', models.CharField(blank=True, help_text='Amount of time required (eg: "30 min commitment")', max_length=256)),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='highlights.Highlight')),
            ],
            options={
                'verbose_name': 'highlight',
                'verbose_name_plural': 'highlights',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipateHighlights2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('commitment', models.CharField(blank=True, help_text='Amount of time required (eg: "30 min commitment")', max_length=256)),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='highlights.Highlight')),
            ],
            options={
                'verbose_name': 'highlight',
                'verbose_name_plural': 'highlights',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipatePage2',
            fields=[
                ('primarypage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.PrimaryPage')),
                ('ctaHeroHeader', models.TextField(blank=True)),
                ('ctaHeroSubhead', wagtail.core.fields.RichTextField(blank=True)),
                ('ctaCommitment', models.TextField(blank=True)),
                ('ctaButtonTitle', models.CharField(blank=True, max_length=250, verbose_name='Button Text')),
                ('ctaButtonURL', models.TextField(blank=True, verbose_name='Button URL')),
                ('ctaHeroHeader2', models.TextField(blank=True)),
                ('ctaHeroSubhead2', wagtail.core.fields.RichTextField(blank=True)),
                ('ctaCommitment2', models.TextField(blank=True)),
                ('ctaButtonTitle2', models.CharField(blank=True, max_length=250, verbose_name='Button Text')),
                ('ctaButtonURL2', models.TextField(blank=True, verbose_name='Button URL')),
                ('ctaHeroHeader3', models.TextField(blank=True)),
                ('ctaHeroSubhead3', wagtail.core.fields.RichTextField(blank=True)),
                ('ctaCommitment3', models.TextField(blank=True)),
                ('ctaFacebook3', models.TextField(blank=True)),
                ('ctaTwitter3', models.TextField(blank=True)),
                ('ctaEmailShareBody3', models.TextField(blank=True)),
                ('ctaEmailShareSubject3', models.TextField(blank=True)),
                ('h2', models.TextField(blank=True)),
                ('h2Subheader', models.TextField(blank=True, verbose_name='H2 Subheader')),
                ('ctaHero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_hero_participate', to='wagtailimages.Image', verbose_name='Primary Hero Image')),
                ('ctaHero2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_hero_participate2', to='wagtailimages.Image', verbose_name='Primary Hero Image')),
                ('ctaHero3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_hero_participate3', to='wagtailimages.Image', verbose_name='Primary Hero Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailpages.primarypage',),
        ),
        migrations.AddField(
            model_name='participatehighlights2',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_highlights2', to='wagtailpages.ParticipatePage2'),
        ),
        migrations.AddField(
            model_name='participatehighlights',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_highlights', to='wagtailpages.ParticipatePage2'),
        ),
        migrations.AddField(
            model_name='cta4',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='cta4', to='wagtailpages.ParticipatePage2'),
        ),
    ]