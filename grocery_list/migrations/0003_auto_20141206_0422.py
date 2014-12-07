# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('grocery_list', '0002_auto_20141205_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
