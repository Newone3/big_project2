# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prispevky', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Prispevky',
        ),
    ]