# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0005_auto_20150320_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('desde', models.DateField(blank=True)),
                ('hasta', models.DateField(blank=True)),
                ('monto_maximo', models.IntegerField(blank=True)),
                ('es_anr', models.BooleanField(default=False)),
                ('web', models.URLField(blank=True)),
                ('observaciones', models.TextField(max_length=2000, blank=True)),
                ('instrumento', models.ForeignKey(to='instrumentos.Instrumento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
