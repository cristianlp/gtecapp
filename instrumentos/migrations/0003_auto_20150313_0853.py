# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0002_auto_20150313_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='desde',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='hasta',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='monto_maximo',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='observaciones',
            field=models.CharField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='web',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
