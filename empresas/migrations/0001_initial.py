# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('telefono', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('ciudad', models.ForeignKey(to='empresas.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
