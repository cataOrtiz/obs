# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0003_comida_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_local', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_pais', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20)),
                ('id_tipo', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tweet', models.IntegerField(default=0)),
                ('fecha', models.DateField(verbose_name=b'date published')),
                ('promocion', models.CharField(max_length=50)),
                ('id_ciudad', models.IntegerField(default=0)),
                ('id_cuenta', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tweet_hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tweet', models.IntegerField(default=0)),
                ('id_hashtag', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='twitero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cuenta', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
