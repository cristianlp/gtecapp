# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0001_initial'),
        ('empresas', '0002_auto_20150326_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_visita', models.DateField()),
                ('motivo', models.TextField(blank=True)),
                ('visitada_por', models.ForeignKey(to='integrantes.Integrante')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
