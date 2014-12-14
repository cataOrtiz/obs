# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0007_auto_20141214_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='id_tipo',
            field=models.ForeignKey(to='observatorio.tipo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comida_local',
            name='id_comida',
            field=models.ForeignKey(to='observatorio.comida'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comida_local',
            name='id_local',
            field=models.ForeignKey(to='observatorio.local'),
            preserve_default=True,
        ),
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
        migrations.AlterField(
            model_name='tweet',
            name='id_ciudad',
            field=models.ForeignKey(to='observatorio.ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id_cuenta',
            field=models.ForeignKey(to='observatorio.twitero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet_hashtag',
            name='id_hashtag',
            field=models.ForeignKey(to='observatorio.hashtag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet_hashtag',
            name='id_tweet',
            field=models.ForeignKey(to='observatorio.tweet'),
            preserve_default=True,
        ),
    ]
