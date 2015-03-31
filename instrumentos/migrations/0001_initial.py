# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desde', models.DateTimeField()),
                ('hasta', models.DateTimeField()),
                ('monto_maximo', models.IntegerField()),
                ('observaciones', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=1000)),
                ('web', models.URLField()),
                ('web_descarga_formularios', models.URLField(blank=True)),
                ('es_anr', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('nivel', models.CharField(default=b'NAC', max_length=3, choices=[(b'NAC', b'Nacional'), (b'PROV', b'Provincial'), (b'MUN', b'Municipal'), (b'INT', b'Internacional')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instrumento',
            name='organismo',
            field=models.ForeignKey(to='instrumentos.Organismo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='instrumento',
            field=models.ForeignKey(to='instrumentos.Instrumento'),
            preserve_default=True,
        ),
    ]
