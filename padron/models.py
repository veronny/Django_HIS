from django.db import models
from filiacion.models import Distrito, Provincia

# Create your models here.
################################################# 
###  SITUACION DEL PADRON NOMINAL
#################################################
class Padron(models.Model):
    cod_padron  = models.CharField(max_length=50,null=True, blank=True)
    cnv = models.CharField(max_length=50,null=True, blank=True)
    cui = models.CharField(max_length=50,null=True, blank=True)
    dni = models.CharField(max_length=50,null=True, blank=True)
    ubigeo  = models.CharField(max_length=50,null=True, blank=True)
    num_doc = models.CharField(max_length=50,null=True, blank=True)
    fecha_nac = models.CharField(max_length=50,null=True, blank=True)
    edad_anio = models.CharField(max_length=50,null=True, blank=True)
    edad_mes = models.CharField(max_length=50,null=True, blank=True)
    edad_dias = models.CharField(max_length=50,null=True, blank=True)
    seguro = models.CharField(max_length=50,null=True, blank=True)
    ap_paterno = models.CharField(max_length=50,null=True, blank=True)
    ap_materno = models.CharField(max_length=50,null=True, blank=True)
    nom_nino = models.CharField(max_length=50,null=True, blank=True)
    direccion = models.CharField(max_length=250,null=True, blank=True)
    eje = models.CharField(max_length=50,null=True, blank=True)
    referencia = models.CharField(max_length=250,null=True, blank=True)
    provincia = models.CharField(max_length=250,null=True, blank=True)
    distrito = models.CharField(max_length=250,null=True, blank=True)
    area = models.CharField(max_length=50,null=True, blank=True)
    visitado = models.CharField(max_length=50,null=True, blank=True)
    fe_visita = models.CharField(max_length=50,null=True, blank=True)
    cod_eess_padron = models.CharField(max_length=50,null=True, blank=True)
    nom_eess_padron = models.CharField(max_length=50,null=True, blank=True)
    frecuencia = models.CharField(max_length=50,null=True, blank=True)
    encontrado = models.CharField(max_length=50,null=True, blank=True)
    dni_mama = models.CharField(max_length=50,null=True, blank=True)
    num_cel = models.CharField(max_length=50,null=True, blank=True)
    pn_reg = models.CharField(max_length=50,null=True, blank=True)
    his_atencion = models.CharField(max_length=50,null=True, blank=True)
    his_eess = models.CharField(max_length=50,null=True, blank=True)
    his_personal = models.CharField(max_length=50,null=True, blank=True)
    edad_mes_actual = models.CharField(max_length=50,null=True, blank=True)
    den = models.IntegerField(null=True, blank=True)
    edad_0_28_dias = models.IntegerField(null=True, blank=True)
    edad_0_5_meses = models.IntegerField(null=True, blank=True)
    edad_6_11_meses = models.IntegerField(null=True, blank=True)
    menores_de_12_meses = models.IntegerField(null=True, blank=True)
    edad_1_anio = models.IntegerField(null=True, blank=True)
    edad_2_anios = models.IntegerField(null=True, blank=True)
    edad_3_anios = models.IntegerField(null=True, blank=True)
    edad_4_anios = models.IntegerField(null=True, blank=True)
    edad_5_anios = models.IntegerField(null=True, blank=True)
    num_num_doc = models.IntegerField(null=True, blank=True)
    num_eje = models.IntegerField(null=True, blank=True)
    num_ref = models.IntegerField(null=True, blank=True)
    num_vis = models.IntegerField(null=True, blank=True)
    num_enc = models.IntegerField(null=True, blank=True)
    num_seguro = models.IntegerField(null=True, blank=True)
    num_nom_eess_padron = models.IntegerField(null=True, blank=True)
    num_num_cel = models.IntegerField(null=True, blank=True)
    num_frecuencia = models.IntegerField(null=True, blank=True)
    num_entidad_eess = models.IntegerField(null=True, blank=True)
    num_entidad_muni = models.IntegerField(null=True, blank=True)
    num_entidad_reniec = models.IntegerField(null=True, blank=True)
    Cod_Red = models.CharField(max_length=250,null=True, blank=True)
    Red = models.CharField(max_length=250,null=True, blank=True)
    Cod_Microred = models.CharField(max_length=250,null=True, blank=True)
    Microred = models.CharField(max_length=250,null=True, blank=True)
    Id_Establecimiento = models.CharField(max_length=250,null=True, blank=True)
    Codigo_Unico = models.CharField(max_length=50,null=True, blank=True)
    Nombre_Establecimiento = models.CharField(max_length=250,null=True, blank=True)
    Numero_Documento_Personal = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.num_doc