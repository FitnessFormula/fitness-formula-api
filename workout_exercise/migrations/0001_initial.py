# Generated by Django 4.1.5 on 2023-01-10 18:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("workout", "0001_initial"),
        ("exercise", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout_exercise",
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
                ("equipment", models.CharField(max_length=120, null=True)),
                ("description", models.TextField(null=True)),
                ("sets", models.PositiveIntegerField()),
                ("reps", models.PositiveIntegerField()),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workouts",
                        to="exercise.exercise",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercises",
                        to="workout.workout",
                    ),
                ),
            ],
        ),
    ]
