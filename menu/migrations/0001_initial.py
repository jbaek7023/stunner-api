# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('menu_type', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('review_count', models.IntegerField(default=0)),
                ('current_rate', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
