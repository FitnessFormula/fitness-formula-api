# Generated by Django 4.1.5 on 2023-01-10 18:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sheet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout",
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
                    "muscle_group",
                    models.CharField(
                        choices=[
                            ("legs", "Choices Legs"),
                            ("arms", "Choices Arms"),
                            ("back", "Choices Back"),
                            ("chest", "Choices Chest"),
                            ("shoulders", "Choices Sholders"),
                            ("cardio", "Choices Cardio"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("monday", "Choices Monday"),
                            ("tuesday", "Choices Tuesday"),
                            ("wednesday", "Choices Wednesday"),
                            ("thursday", "Choices Thursday"),
                            ("friday", "Choices Friday"),
                            ("saturday", "Choices Saturday"),
                            ("sunday", "Choices Sunday"),
                        ],
                        max_length=10,
                    ),
                ),
                ("title", models.CharField(max_length=120, null=True)),
                ("description", models.TextField(null=True)),
                (
                    "sheet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sheet",
                        to="sheet.sheet",
                    ),
                ),
            ],
        ),
    ]
