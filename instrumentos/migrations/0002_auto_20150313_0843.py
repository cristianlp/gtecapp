# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrumento',
            old_name='web_descarga_formularios',
            new_name='web_formularios',
        ),
    ]
