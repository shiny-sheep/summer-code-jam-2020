# Generated by Django 3.0.9 on 2020-08-07 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0006_remove_project_preview_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='date_last_modified',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
    ]
