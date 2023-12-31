# Generated by Django 4.0.6 on 2023-11-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filiacion', '0004_visita'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Anio', models.CharField(blank=True, max_length=200, null=True)),
                ('Mes', models.CharField(blank=True, max_length=200, null=True)),
                ('Dia', models.CharField(blank=True, max_length=200, null=True)),
                ('Fecha_Atencion', models.CharField(blank=True, max_length=200, null=True)),
                ('Codigo_Red', models.CharField(blank=True, max_length=200, null=True)),
                ('Red', models.CharField(blank=True, max_length=200, null=True)),
                ('Codigo_MicroRed', models.CharField(blank=True, max_length=200, null=True)),
                ('MicroRed', models.CharField(blank=True, max_length=200, null=True)),
                ('Codigo_Unico', models.CharField(blank=True, max_length=200, null=True)),
                ('Nombre_Establecimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('Id_Establecimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('DIS_EVALUACION', models.IntegerField(blank=True, null=True)),
                ('DIS_CALIFICACION', models.IntegerField(blank=True, null=True)),
                ('DIS_LEV', models.IntegerField(blank=True, null=True)),
                ('DIS_MOD', models.IntegerField(blank=True, null=True)),
                ('DIS_SEV', models.IntegerField(blank=True, null=True)),
                ('DIS_TOTAL', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
