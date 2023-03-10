# Generated by Django 4.1.5 on 2023-01-10 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sheet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("hypertrophy", "Hypertrophy"),
                            ("fat_loss", "Fat Loss"),
                            ("keep_in_shape", "Keep In Shape"),
                            ("bodybuilder", "Bodybuilder"),
                        ],
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("until", models.DateField()),
            ],
        ),
    ]
