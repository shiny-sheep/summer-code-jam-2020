# Generated by Django 3.0.8 on 2020-08-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rovers", "0003_auto_20200801_1217"),
    ]

    operations = [
        migrations.RemoveField(model_name="rover", name="username",),
        migrations.AddField(
            model_name="rover",
            name="user_name",
            field=models.SlugField(default="xXcuriosity02Xx"),
            preserve_default=False,
        ),
    ]