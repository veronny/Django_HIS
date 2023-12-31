# Generated by Django 4.1.5 on 2023-11-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0006_alter_rpt_certificado_fecha_atencion"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActualizaBD",
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
                (
                    "fecha_plano",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("hora_plano", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "fecha_paciente",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_paciente",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "fecha_personal",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_personal",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "fecha_padron",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_padron",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "fecha_certificado",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "hora_certificado",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
    ]
