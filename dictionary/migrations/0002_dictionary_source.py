# Generated by Django 4.0.3 on 2022-03-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dictionary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dictionary",
            name="source",
            field=models.CharField(
                choices=[("en", "English"), ("en-us", "Ameracan English")], default="en-us", max_length=50
            ),
        ),
    ]