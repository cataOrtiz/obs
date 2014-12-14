# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observatorio', '0002_comida'),
    ]

    operations = [
        migrations.CreateModel(
            name='comida_local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_comida', models.IntegerField(default=0)),
                ('id_local', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
