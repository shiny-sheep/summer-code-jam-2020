# Generated by Django 3.0.8 on 2020-08-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rovers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rover",
            name="username",
            field=models.CharField(
                default=models.CharField(max_length=50), max_length=50
            ),
        ),
    ]
