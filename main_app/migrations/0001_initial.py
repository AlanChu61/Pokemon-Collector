# Generated by Django 4.1.7 on 2023-04-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pokmon_id", models.IntegerField(default=0)),
                ("img", models.CharField(max_length=250)),
            ],
        ),
    ]
