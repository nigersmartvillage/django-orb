# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-08-29 10:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='attribution_fr',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='title_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resourcecriteria',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resourcefile',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcefile',
            name='title_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourceurl',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourceurl',
            name='title_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='description_fr',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='summary_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
