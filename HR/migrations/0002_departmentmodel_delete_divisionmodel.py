# Generated by Django 4.2.4 on 2023-09-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HR", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepartmentModel",
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
                ("Dept_name", models.CharField(max_length=200)),
                ("create_by", models.CharField(max_length=200)),
                ("updatedby", models.CharField(max_length=200)),
                ("pc_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="DivisionModel",
        ),
    ]
