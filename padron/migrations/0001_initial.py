# Generated by Django 4.1.5 on 2024-02-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RptVisita",
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
                ("ubigeo", models.CharField(blank=True, max_length=50, null=True)),
                ("cnv", models.CharField(blank=True, max_length=50, null=True)),
                ("cui", models.CharField(blank=True, max_length=50, null=True)),
                ("dni", models.CharField(blank=True, max_length=50, null=True)),
                ("num_doc", models.CharField(blank=True, max_length=50, null=True)),
                ("fecha_nac", models.CharField(blank=True, max_length=50, null=True)),
                ("ap_paterno", models.CharField(blank=True, max_length=50, null=True)),
                ("ap_materno", models.CharField(blank=True, max_length=50, null=True)),
                ("nom_nino", models.CharField(blank=True, max_length=50, null=True)),
                ("direccion", models.CharField(blank=True, max_length=250, null=True)),
                ("eje", models.CharField(blank=True, max_length=50, null=True)),
                ("referencia", models.CharField(blank=True, max_length=250, null=True)),
                ("provincia", models.CharField(blank=True, max_length=250, null=True)),
                ("distrito", models.CharField(blank=True, max_length=250, null=True)),
                ("area", models.CharField(blank=True, max_length=50, null=True)),
                ("visitado", models.CharField(blank=True, max_length=50, null=True)),
                ("fe_visita", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "cod_eess_padron",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "nom_eess_padron",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("encontrado", models.IntegerField(blank=True, null=True)),
                ("dni_mama", models.CharField(blank=True, max_length=50, null=True)),
                ("num_cel", models.CharField(blank=True, max_length=50, null=True)),
                ("pn_reg", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "his_atencion",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("his_eess", models.IntegerField(blank=True, null=True)),
                ("his_personal", models.IntegerField(blank=True, null=True)),
                ("edad_mes", models.IntegerField(blank=True, null=True)),
                ("den", models.IntegerField(blank=True, null=True)),
                ("num_num_doc", models.CharField(blank=True, max_length=50, null=True)),
                ("num_eje", models.CharField(blank=True, max_length=50, null=True)),
                ("num_ref", models.CharField(blank=True, max_length=50, null=True)),
                ("num_vis", models.CharField(blank=True, max_length=50, null=True)),
                ("num_enc", models.CharField(blank=True, max_length=50, null=True)),
                ("seguro", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "num_nom_eess_padron",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("num_num_cel", models.CharField(blank=True, max_length=50, null=True)),
                ("frecuencia", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "num_entidad_eess",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "num_entidad_muni",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "num_entidad_reniec",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("Red", models.CharField(blank=True, max_length=250, null=True)),
                ("Microred", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "Codigo_Unico",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "Nombre_Establecimiento",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "Numero_Documento_Personal",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
        ),
    ]