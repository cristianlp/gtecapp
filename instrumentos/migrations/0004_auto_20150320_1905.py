# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0003_auto_20150313_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='es_anr',
        ),
        migrations.RemoveField(
            model_name='instrumento',
            name='web_formularios',
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='es_anr',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='web',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='observaciones',
            field=models.TextField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='descripcion',
            field=models.TextField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
