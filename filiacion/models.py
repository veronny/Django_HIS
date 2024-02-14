from django.db import models

class TipoReporte(models.Model):
    nombre = models.CharField(max_length=50)  
class Diresa(models.Model):
    nombre_diresa = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_diresa = models.CharField(max_length=10, default="", null=True, blank=True)
    def __str__(self):
        return self.nombre_diresa   
class Red(models.Model):
    nombre_red = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="", null=True, blank=True)
    def __str__(self):
        return self.nombre_red   
class Microred(models.Model):
    nombre_microred = models.CharField(max_length=200,null=True, blank=True)
    cod_microred = models.CharField(max_length=100, default="",null=True, blank=True)
    cod_red = models.CharField(max_length=100, default="",null=True, blank=True)
    red_microred = models.CharField(max_length=100, default="",null=True, blank=True)
    def __str__(self):
        return self.nombre_microred  
class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=100, null=True, blank=True)
    codigo_unico = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_red = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_microred = models.CharField(max_length=100, default="", null=True, blank=True)
    red_microred = models.CharField(max_length=100, default="",null=True, blank=True)
    def __str__(self):
        return self.nombre_establecimiento 
class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=100,null=True, blank=True)
    ubigeo = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre_provincia        
class Distrito(models.Model):
    nombre_distrito = models.CharField(max_length=100, null=True, blank=True)
    ubigeo_dis = models.CharField(max_length=100, null=True, blank=True) 
    cod_provincia = models.CharField(max_length=100, null=True, blank=True) 
    def __str__(self):
        return self.nombre_distrito
class Filiacion(models.Model):
    TIPO_MUNICIPALIDAD = [
                ('Provincial', 'Provincial'),
                ('Distrital', 'Distrital'),
            ]
    
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    provincia = models.CharField(max_length=100,null=True, blank=True)
    distrito = models.CharField(max_length=100,null=True, blank=True)
    tipo_municipalidad = models.CharField(choices=TIPO_MUNICIPALIDAD, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
class Directorio(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class DirectorioRed(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class DirectorioEstablecimiento(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres

class Visita(models.Model):
    # Otros campos de tu modelo
    visitas = models.PositiveIntegerField(default=0)

class ActualizaBD(models.Model):
    fecha_plano = models.CharField(max_length=100,null=True, blank=True)
    hora_plano = models.CharField(max_length=100,null=True, blank=True)
    fecha_paciente = models.CharField(max_length=100,null=True, blank=True)
    hora_paciente = models.CharField(max_length=100,null=True, blank=True)
    fecha_personal = models.CharField(max_length=100,null=True, blank=True)
    hora_personal = models.CharField(max_length=100,null=True, blank=True)
    fecha_padron = models.CharField(max_length=100,null=True, blank=True)
    hora_padron = models.CharField(max_length=100,null=True, blank=True)
    fecha_certificado = models.CharField(max_length=100,null=True, blank=True)
    hora_certificado = models.CharField(max_length=100,null=True, blank=True)

#################################################
###  CETIFICACIONES
#################################################
class rpt_certificado(models.Model):
    Anio = models.CharField(max_length=200,null=True, blank=True)
    Mes = models.CharField(max_length=200,null=True, blank=True)
    Dia = models.CharField(max_length=200,null=True, blank=True)
    Fecha_Atencion =  models.DateField(max_length=100,null=True, blank=True)
    Codigo_Red = models.CharField(max_length=200,null=True, blank=True)
    Red = models.CharField(max_length=200,null=True, blank=True)
    Codigo_MicroRed = models.CharField(max_length=200,null=True, blank=True)
    MicroRed = models.CharField(max_length=200,null=True, blank=True)
    Codigo_Unico = models.CharField(max_length=200,null=True, blank=True)
    Nombre_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    Id_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    DIS_EVALUACION = models.IntegerField(blank=True, null=True)
    DIS_CALIFICACION = models.IntegerField(blank=True, null=True)
    DIS_LEV = models.IntegerField(blank=True, null=True)
    DIS_MOD = models.IntegerField(blank=True, null=True)
    DIS_SEV = models.IntegerField(blank=True, null=True)
    DIS_TOTAL = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.Id_Establecimiento
    
class RptVisitaDis(models.Model):
    Anio = models.CharField(max_length=200,null=True, blank=True)
    Mes = models.CharField(max_length=200,null=True, blank=True)
    Dia = models.CharField(max_length=200,null=True, blank=True)
    Fecha_Atencion =  models.DateField(max_length=100,null=True, blank=True)
    Codigo_Red = models.CharField(max_length=200,null=True, blank=True)
    Red = models.CharField(max_length=200,null=True, blank=True)
    Codigo_MicroRed = models.CharField(max_length=200,null=True, blank=True)
    MicroRed = models.CharField(max_length=200,null=True, blank=True)
    Codigo_Unico = models.CharField(max_length=200,null=True, blank=True)
    Nombre_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    Id_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    VISITA_1 = models.IntegerField(blank=True, null=True)
    VISITA_2 = models.IntegerField(blank=True, null=True)
    VISITA_3 = models.IntegerField(blank=True, null=True)
    VISITA_4 = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.Id_Establecimiento

class RptSeguimientoVisitaDis(models.Model):
    Codigo_Red = models.CharField(max_length=200,null=True, blank=True)
    Red = models.CharField(max_length=200,null=True, blank=True)
    Codigo_MicroRed = models.CharField(max_length=200,null=True, blank=True)
    MicroRed = models.CharField(max_length=200,null=True, blank=True)
    Codigo_Unico = models.CharField(max_length=200,null=True, blank=True)
    Nombre_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    Id_Establecimiento = models.CharField(max_length=200,null=True, blank=True)
    Numero_Documento_Paciente = models.CharField(max_length=200,null=True, blank=True)
    FECHA_VISITA_1 = models.DateField(max_length=100,null=True, blank=True)
    EESS_VISITA_1 =	models.CharField(max_length=200,null=True, blank=True)
    FECHA_VISITA_2 = models.DateField(max_length=100,null=True, blank=True)	
    EESS_VISITA_2 =	models.CharField(max_length=200,null=True, blank=True)
    FECHA_VISITA_3 = models.DateField(max_length=100,null=True, blank=True)	
    EESS_VISITA_3 =	models.CharField(max_length=200,null=True, blank=True)
    FECHA_VISITA_4 = models.DateField(max_length=100,null=True, blank=True)	
    EESS_VISITA_4 = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.Id_Establecimiento

################################################# 
###  PADRON NOMINAL 
#################################################
class Item_mes(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

################################################# 
###  INDICADOR VISITA DOMICILARIA 
#################################################
class RptVisita(models.Model):
    ubigeo  = models.CharField(max_length=50,null=True, blank=True)
    edad_mes = models.CharField(max_length=50,null=True, blank=True)
    año = models.CharField(max_length=50,null=True, blank=True)
    mes = models.CharField(max_length=50,null=True, blank=True)
    num_doc = models.CharField(max_length=50,null=True, blank=True)
    fecha_nac = models.CharField(max_length=50,null=True, blank=True)
    seguro = models.CharField(max_length=50,null=True, blank=True)
    ap_paterno = models.CharField(max_length=50,null=True, blank=True)
    ap_materno = models.CharField(max_length=50,null=True, blank=True)
    nom_nino = models.CharField(max_length=50,null=True, blank=True)
    direccion = models.CharField(max_length=250,null=True, blank=True)
    visitado = models.CharField(max_length=50,null=True, blank=True)
    encontrado = models.CharField(max_length=50,null=True, blank=True)
    dni_mama = models.CharField(max_length=50,null=True, blank=True)
    num_cel = models.CharField(max_length=50,null=True, blank=True)
    pn_reg = models.CharField(max_length=50,null=True, blank=True)
    Id_Establecimiento = models.CharField(max_length=50,null=True, blank=True)
    den = models.IntegerField(null=True, blank=True)
    num =models.IntegerField(null=True, blank=True)
    renaes1 = models.CharField(max_length=50,null=True, blank=True)
    renaes2 = models.CharField(max_length=50,null=True, blank=True)
    renaes3 = models.CharField(max_length=50,null=True, blank=True)
    renaes4 = models.CharField(max_length=50,null=True, blank=True)
    visita1 = models.IntegerField(null=True, blank=True)
    visita2 = models.IntegerField(null=True, blank=True)
    visita3 = models.IntegerField(null=True, blank=True)
    visita4 = models.IntegerField(null=True, blank=True)
    v_fecha1 = models.CharField(max_length=50,null=True, blank=True)
    v_fecha2 = models.CharField(max_length=50,null=True, blank=True)
    v_fecha3 = models.CharField(max_length=50,null=True, blank=True)
    v_fecha4 = models.CharField(max_length=50,null=True, blank=True)
    Codigo_Provincia_Inei = models.CharField(max_length=50,null=True, blank=True)
    Provincia = models.CharField(max_length=50,null=True, blank=True)
    Codigo_Distrito_Inei = models.CharField(max_length=50,null=True, blank=True)
    Distrito = models.CharField(max_length=50,null=True, blank=True)
    Codigo_Red = models.CharField(max_length=50,null=True, blank=True)
    Red = models.CharField(max_length=50,null=True, blank=True)
    Codigo_MicroRed = models.CharField(max_length=50,null=True, blank=True)
    MicroRed = models.CharField(max_length=50,null=True, blank=True)
    Codigo_Unico = models.CharField(max_length=50,null=True, blank=True)
    Nombre_Establecimiento = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.num_doc