# Generated by Django 4.1.5 on 2024-02-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("padron", "0002_rename_rptvisita_padron"),
    ]

    operations = [
        migrations.AddField(
            model_name="padron",
            name="num_frecuencia",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="padron",
            name="num_seguro",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="edad_mes",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="encontrado",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="his_eess",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="his_personal",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_eje",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_enc",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_entidad_eess",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_entidad_muni",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_entidad_reniec",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_nom_eess_padron",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_num_cel",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_num_doc",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_ref",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="padron",
            name="num_vis",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
