from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Filiacion, Red, Microred, Establecimiento, Provincia, Distrito, Directorio, DirectorioRed, DirectorioEstablecimiento, rpt_certificado, ActualizaBD, RptVisitaDis, RptSeguimientoVisitaDis, TipoReporte

#--------------DIRECTORIO DE MUNICIPIO --------------------------
class FiliacionResources(resources.ModelResource):
    class Meta:
        model = Filiacion

@admin.register(Filiacion)
class FiliacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = FiliacionResources
    list_display = (
        'provincia',
        'distrito',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
        'condicion',
        'cuenta_usuario'
    )
    search_fields = ('nombres',)
 
#--------------DIRECTORIO DE DIRESA --------------------------
class DirectorioResources(resources.ModelResource):
    class Meta:
        model = Directorio

@admin.register(Directorio)
class DirectorioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DirectorioResources
    list_display = (
        'diresa',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
        'condicion',
        'cuenta_usuario'
    )
    search_fields = ('nombres',)
    
#--------------DIRECTORIO DE REDES --------------------------
class DirectorioRedResources(resources.ModelResource):
    class Meta:
        model = DirectorioRed

@admin.register(DirectorioRed)
class DirectorioRedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DirectorioRedResources
    list_display = (
        'diresa',
        'red',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
        'condicion',
        'cuenta_usuario'
    )
    search_fields = ('nombres',)

#--------------DIRECTORIO DE ESTABLECIMIENTO --------------------------
class DirectorioEstablecimientoResources(resources.ModelResource):
    class Meta:
        model = DirectorioEstablecimiento

@admin.register(DirectorioEstablecimiento)
class DirectorioEstablecimientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DirectorioEstablecimientoResources
    list_display = (
        'diresa',
        'red',
        'microred',
        'establecimiento',
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
        'condicion',
        'cuenta_usuario'
    )
    search_fields = ('nombres',)
    
###################################################### 
#-------------- REPORTE DE DISCAPACIDAD --------------
class RptCertificadoResources(resources.ModelResource):
    class Meta:
        model = rpt_certificado

@admin.register(rpt_certificado)
class RptCertificadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RptCertificadoResources
    list_display = (                                                          
                    'Anio',
                    'Mes',
                    'Dia',
                    'Fecha_Atencion',
                    'Codigo_Red',
                    'Red',
                    'Codigo_MicroRed',
                    'MicroRed',
                    'Codigo_Unico',
                    'Nombre_Establecimiento',
                    'Id_Establecimiento',
                    'DIS_EVALUACION',
                    'DIS_CALIFICACION',
                    'DIS_LEV',
                    'DIS_MOD',
                    'DIS_SEV',
                    'DIS_TOTAL'
    )
    search_fields = ('id','Red','MicroRed','Nombre_Establecimiento','DIS_EVALUACION','DIS_CALIFICACION','DIS_LEV','DIS_MOD','DIS_SEV','DIS_TOTAL',)    

###################################################### 
#-------------- ACTUALIZAR FECHAS --------------------
class ActualizaBDResources(resources.ModelResource):
    class Meta:
        model = ActualizaBD

@admin.register(ActualizaBD)
class ActualizaBDAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ActualizaBDResources
    list_display = (                                                          
                    'fecha_plano', 
                    'hora_plano',
                    'fecha_paciente',
                    'hora_paciente',
                    'fecha_personal',
                    'hora_personal',
                    'fecha_padron',
                    'hora_padron',
                    'fecha_certificado',
                    'hora_certificado'
    )   
###################################################### 
#---- REPORTE DE VISITAS DE DISCAPACIDAD -------------
class RptVisitaDisResources(resources.ModelResource):
    class Meta:
        model = RptVisitaDis

@admin.register(RptVisitaDis)
class RptVisitaDisAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RptVisitaDisResources
    list_display = (                                                          
                    'Anio',
                    'Mes',
                    'Dia',
                    'Fecha_Atencion',
                    'Codigo_Red',
                    'Red',
                    'Codigo_MicroRed',
                    'MicroRed',
                    'Codigo_Unico',
                    'Nombre_Establecimiento',
                    'Id_Establecimiento',
                    'VISITA_1',
                    'VISITA_2',
                    'VISITA_3',
                    'VISITA_4'
    )
    search_fields = ('id','Red','MicroRed','Nombre_Establecimiento','VISITA_1','VISITA_2','VISITA_3','VISITA_4',)    

###################################################### 
#---- REPORTE DE SEGUIMIENTO VISITAS DE DISCAPACIDAD -------------
class RptSeguimientoVisitaDisResources(resources.ModelResource):
    class Meta:
        model = RptSeguimientoVisitaDis

@admin.register(RptSeguimientoVisitaDis)
class RptSeguimientoVisitaDisAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RptSeguimientoVisitaDisResources
    list_display = (                                                          
                    'Codigo_Red',
                    'Red', 
                    'Codigo_MicroRed',
                    'MicroRed',
                    'Codigo_Unico',
                    'Nombre_Establecimiento',
                    'Id_Establecimiento',
                    'Numero_Documento_Paciente',
                    'FECHA_VISITA_1', 
                    'EESS_VISITA_1', 
                    'FECHA_VISITA_2',	
                    'EESS_VISITA_2',
                    'FECHA_VISITA_3',	
                    'EESS_VISITA_3',
                    'FECHA_VISITA_4',	
                    'EESS_VISITA_4'
    )
    search_fields = ('id','Red','MicroRed','Nombre_Establecimiento','FECHA_VISITA_1','EESS_VISITA_1','FECHA_VISITA_2','EESS_VISITA_2','FECHA_VISITA_3','EESS_VISITA_3','FECHA_VISITA_4','EESS_VISITA_4',)  
    
###################################################### 
#----  TIPO DE REPORTE -------------
class TipoReporteResources(resources.ModelResource):
    class Meta:
        model = TipoReporte

@admin.register(TipoReporte)
class TipoReporteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = TipoReporteResources
    list_display = (                                                          
                    'id',
                    'nombre', 

    )
    search_fields = ('id','nombre',)  
    
###################################################### 
#----  PROVINCIA -------------
class ProvinciaResources(resources.ModelResource):
    class Meta:
        model = Provincia

@admin.register(Provincia)
class ProvinciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ProvinciaResources
    list_display = (                                                          
                    'id',
                    'nombre_provincia', 
                    'ubigeo', 
    )
    search_fields = ('id','nombre_provincia','ubigeo',)  

###################################################### 
#----  DISTRITO -------------
class DistritoResources(resources.ModelResource):
    class Meta:
        model = Distrito

@admin.register(Distrito)
class DistritoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DistritoResources
    list_display = (                                                          
                    'id',
                    'nombre_distrito', 
                    'ubigeo_dis', 
                    'cod_provincia'
    )
    search_fields = ('id','nombre_distrito','ubigeo_dis','cod_provincia',)  

###################################################### 
#----  RED  -------------
class RedResources(resources.ModelResource):
    class Meta:
        model = Red

@admin.register(Red)
class RedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RedResources
    list_display = (                                                          
                    'id',
                    'nombre_red', 
                    'cod_red', 
    )
    search_fields = ('id','nombre_red','cod_red',)  

###################################################### 
#----  MICRORED  -------------
class MicroredResources(resources.ModelResource):
    class Meta:
        model = Microred

@admin.register(Microred)
class MicroredAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = MicroredResources
    list_display = (                                                          
                    'id',
                    'nombre_microred',
                    'cod_microred', 
                    'cod_red', 
                    'red_microred',
    )
    search_fields = ('id','nombre_microred','cod_microred','cod_red','red_microred',)  
 

###################################################### 
#----  ESTABLECIMIENTOS -------------
class EstablecimientoResources(resources.ModelResource):
    class Meta:
        model = Establecimiento

@admin.register(Establecimiento)
class EstablecimientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EstablecimientoResources
    list_display = (                                                          
                    'id',
                    'nombre_establecimiento', 
                    'codigo_unico', 
                    'cod_red', 
                    'cod_microred', 
                    'red_microred',
    )
    search_fields = ('id','nombre_establecimiento','codigo_unico','cod_red','cod_microred','red_microred',)  
    
    