# Generated by Django 3.0.8 on 2020-08-01 20:20

import page_maker.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('page_maker', '0002_auto_20200801_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='style_sheet',
            field=models.FilePathField(match='.*\\.css$', path=page_maker.models.get_theme_path,
                                       recursive=True),
        ),
    ]
