# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0004_auto_20150320_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convocatoria',
            name='instrumento',
        ),
        migrations.DeleteModel(
            name='Convocatoria',
        ),
    ]
