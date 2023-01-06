# Generated by Django 4.1.5 on 2023-01-05 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0001_initial"),
        ("workout_exercise", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workout_exercise",
            name="workout",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to="workout.workout",
            ),
        ),
    ]
