# Generated by Django 4.2.3 on 2024-02-07 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="waitlistemail",
            name="email",
            field=models.CharField(max_length=130, unique=True),
        ),
    ]
