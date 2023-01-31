# Generated by Django 4.1.5 on 2023-01-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0009_filiacion_datetimeofupload_generales_excel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filiacion",
            name="req_formato",
            field=models.FileField(upload_to="filiacion/formato/"),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="req_generales_excel",
            field=models.FileField(upload_to="filiacion/excel/"),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="req_oficio",
            field=models.FileField(upload_to="filiacion/oficio"),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="req_resolucion",
            field=models.FileField(upload_to="filiacion/resolucion/"),
        ),
    ]