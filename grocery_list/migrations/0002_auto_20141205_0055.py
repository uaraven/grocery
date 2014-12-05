# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='item_name',
            new_name='record_name',
        ),
    ]
