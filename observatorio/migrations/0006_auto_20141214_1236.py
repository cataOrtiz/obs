# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0005_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
