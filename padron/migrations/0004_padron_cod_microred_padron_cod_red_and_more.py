# Generated by Django 4.1.5 on 2024-02-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("padron", "0003_padron_num_frecuencia_padron_num_seguro_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="padron",
            name="Cod_Microred",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="padron",
            name="Cod_Red",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="padron",
            name="Id_Establecimiento",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="padron",
            name="cod_padron",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
