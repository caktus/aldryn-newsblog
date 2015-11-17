# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields
import app_data.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0005_auto_20150807_0207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsblogconfig',
            options={'verbose_name_plural': 'configs', 'verbose_name': 'config'},
        ),
        migrations.AlterModelOptions(
            name='newsblogconfigtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'config Translation'},
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='lead_in',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', help_text='Optional. Will be displayed in lists, and at the start of the detail page (in bold)', blank=True, verbose_name='lead-in'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='app_data',
            field=app_data.fields.AppDataField(default='{}', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='template_prefix',
            field=models.CharField(null=True, max_length=20, blank=True, verbose_name='Prefix for template dirs'),
            preserve_default=True,
        ),
    ]
