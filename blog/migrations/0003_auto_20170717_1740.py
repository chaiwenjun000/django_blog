# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]
