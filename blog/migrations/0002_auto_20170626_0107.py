# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_text',
            new_name='content',
        ),
    ]