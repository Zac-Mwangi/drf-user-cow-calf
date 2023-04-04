# Generated by Django 4.2 on 2023-04-04 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth_client", "0002_userscows"),
    ]

    operations = [
        migrations.CreateModel(
            name="UsersCalves",
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
                ("calf_name", models.CharField(max_length=255)),
                ("calf_breed", models.CharField(max_length=255)),
                ("createdAt", models.DateField(auto_now_add=True)),
                ("updatedAt", models.DateField(auto_now=True)),
                (
                    "calf_cow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_client.userscows",
                    ),
                ),
                (
                    "calf_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_client.users",
                    ),
                ),
            ],
        ),
    ]