# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0008_auto_20141214_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida_tweet',
            name='id_comida',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comida_tweet',
            name='id_tweet',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
