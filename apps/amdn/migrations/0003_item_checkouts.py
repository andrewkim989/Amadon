# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-18 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amdn', '0002_auto_20180717_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='checkouts',
            field=models.ManyToManyField(related_name='items', to='amdn.Checkout'),
        ),
    ]
