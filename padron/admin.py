from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Padron
###################################################### 
#----  RED  -------------
class PadronResources(resources.ModelResource):
    class Meta:
        model = Padron

@admin.register(Padron)
class PadronAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = PadronResources
    list_display = (                                                          
                    'ubigeo',  
                    'cnv',
                    'cui',
                    'dni',
                    'num_doc',
                    'fecha_nac',
                    'seguro',
                    'ap_paterno',
                    'ap_materno',
                    'nom_nino',
                    'direccion',
                    'eje',
                    'referencia',
                    'provincia',
                    'distrito',
                    'area',
                    'visitado',
                    'fe_visita',
                    'cod_eess_padron',
                    'nom_eess_padron',
                    'frecuencia',
                    'encontrado',
                    'dni_mama',
                    'num_cel',
                    'pn_reg',
                    'his_atencion',
                    'his_eess',
                    'his_personal',
                    'edad_mes',
                    'den',
                    'num_num_doc',
                    'num_eje',
                    'num_ref',
                    'num_vis',
                    'num_enc',
                    'seguro',
                    'num_nom_eess_padron',
                    'num_num_cel',
                    'frecuencia',
                    'num_entidad_eess',
                    'num_entidad_muni',
                    'num_entidad_reniec',
                    'Red',
                    'Microred',
                    'Codigo_Unico',
                    'Nombre_Establecimiento',
                    'Numero_Documento_Personal',
                    )
    search_fields = ('ubigeo','cnv','cui','dni','num_doc','fecha_nac','seguro','ap_paterno','ap_materno','nom_nino','direccion','eje','referencia','provincia','distrito','area',
                    'visitado','fe_visita','cod_eess_padron','nom_eess_padron','frecuencia','encontrado','dni_mama','num_cel','pn_reg','his_atencion','his_eess','his_personal',
                    'edad_mes','den','num_num_doc','num_eje','num_ref','num_vis','num_enc','seguro','num_nom_eess_padron','num_num_cel','frecuencia','num_entidad_eess','num_entidad_muni',
                    'num_entidad_reniec','Red','Microred','Codigo_Unico','Nombre_Establecimiento','Numero_Documento_Personal',)  

###################################################### 
# Register your models here.
