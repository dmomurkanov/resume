# Generated by Django 5.1.2 on 2024-10-15 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainpage", "0006_portfolio"),
    ]

    operations = [
        migrations.AddField(
            model_name="additionalinfo",
            name="personal",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mainpage.personalinfo",
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="resume_file",
            field=models.FileField(upload_to="personal", verbose_name="Файл резюме"),
        ),
    ]