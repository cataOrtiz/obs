# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0009_auto_20141214_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida_tweet',
            name='id_comida',
            field=models.ForeignKey(to='observatorio.comida'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comida_tweet',
            name='id_tweet',
            field=models.ForeignKey(to='observatorio.tweet'),
            preserve_default=True,
        ),
    ]
