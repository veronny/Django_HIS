# Generated by Django 4.1.5 on 2023-01-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "filiacion",
            "0012_alter_filiacion_distrito_alter_filiacion_provincia_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="filiacion",
            name="dateTimeOfUpload_generales_excel",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="dateTimeOfUpload_req_formato",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="dateTimeOfUpload_req_oficio",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="dateTimeOfUpload_req_resolucion",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]