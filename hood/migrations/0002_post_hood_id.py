# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hood_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.NeighbourHood'),
        ),
    ]
