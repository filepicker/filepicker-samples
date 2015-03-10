# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_filepicker.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(unique=True, max_length=255)),
                ('fpfile', django_filepicker.models.FPFileField(upload_to=b'uploads')),
                ('fpfile_url', models.URLField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
