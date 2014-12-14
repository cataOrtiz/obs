# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0006_auto_20141214_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='id_pais',
            field=models.ForeignKey(to='observatorio.pais'),
            preserve_default=True,
        ),
    ]
