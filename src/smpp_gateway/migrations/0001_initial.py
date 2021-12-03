# Generated by Django 2.2.24 on 2021-12-03 04:06

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rapidsms", "0004_auto_20150801_2138"),
    ]

    operations = [
        migrations.CreateModel(
            name="MTMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_time", models.DateTimeField()),
                ("modify_time", models.DateTimeField()),
                ("short_message", models.TextField()),
                ("params", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("sending", "Sending"),
                            ("sent", "Sent"),
                            ("delivered", "Delivered"),
                            ("error", "Error"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "backend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="rapidsms.Backend",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MOMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_time", models.DateTimeField()),
                ("modify_time", models.DateTimeField()),
                ("short_message", models.BinaryField()),
                ("params", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("processing", "Processing"),
                            ("done", "Done"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "backend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="rapidsms.Backend",
                    ),
                ),
            ],
        ),
    ]
