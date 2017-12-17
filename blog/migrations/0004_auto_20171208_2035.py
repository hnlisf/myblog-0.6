#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 12:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171208_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url_width',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post.jpg', upload_to='avatar/post/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]
