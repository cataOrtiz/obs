# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0004_local_pais_tipo_tweet_tweet_hashtag_twitero'),
    ]

    operations = [
        migrations.CreateModel(
            name='hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_hashtag', models.IntegerField(default=0)),
                ('texto', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
