# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-10 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0002_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
