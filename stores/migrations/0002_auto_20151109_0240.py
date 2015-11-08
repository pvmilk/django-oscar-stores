# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/store-images', verbose_name='Image', null=True),
        ),
        migrations.AlterField(
            model_name='storeaddress',
            name='title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Title', choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')]),
        ),
    ]
