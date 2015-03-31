# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0006_convocatoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='es_anr',
            field=models.BooleanField(default=False, verbose_name=b'Es ANR?'),
            preserve_default=True,
        ),
    ]
