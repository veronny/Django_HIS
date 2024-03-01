from django.urls import path
from . import views
from .views import RptProvinciaPadron, get_provincias_padron, get_distritos_padron, p_distritos_padron, RptDistritoPadron

app_name = 'padron'

urlpatterns = [
    # Padron Nominal
    path('padron_situacion/', views.index, name='padron_situacion'),    
    # graficos edades
    path('padron_situacion/get_chart_padron_edades/', views.get_chart_padron_edades, name='get_chart_padron_edades'),
    # graficos SEXO
    path('padron_situacion/get_chart_padron_sexo/', views.get_chart_padron_sexo, name='get_chart_padron_sexo'),
    # graficos sin DNI
    path('padron_situacion/get_chart_padron_dni/', views.get_chart_padron_dni, name='get_chart_padron_dni'),
    # graficos sin SEGURO
    path('padron_situacion/get_chart_padron_seguro/', views.get_chart_padron_seguro, name='get_chart_padron_seguro'),
    # graficos sin ENCONTRADO
    path('padron_situacion/get_chart_padron_encontrado/', views.get_chart_padron_encontrado, name='get_chart_padron_encontrado'),
    # graficos sin VISITADO
    path('padron_situacion/get_chart_padron_visitado/', views.get_chart_padron_visitado, name='get_chart_padron_visitado'),
    # graficos sin CELULAR
    path('padron_situacion/get_chart_padron_celular/', views.get_chart_padron_celular, name='get_chart_padron_celular'),
    # graficos sin FRECUENCIA
    path('padron_situacion/get_chart_padron_frecuencia/', views.get_chart_padron_frecuencia, name='get_chart_padron_frecuencia'),
    # graficos sin ENTIDAD
    path('padron_situacion/get_chart_padron_entidad/', views.get_chart_padron_entidad, name='get_chart_padron_emtidad'),
    # graficos sin HIS MINSA
    path('padron_situacion/get_chart_padron_atencion/', views.get_chart_padron_atencion, name='get_chart_padron_atencion'),     #-- provincia excel
    ####################################
    ### SEGUIMIENTO
    ####################################
    # Padron provincia
    path('padron_situacion/get_provincias_padron/<int:provincias_id>/', get_provincias_padron, name='get_provincias_padron'),
    # Padron provincia excel
    path('rpt_provincia_padron/', RptProvinciaPadron.as_view() , name = 'rpt_prov_padron_xls'),   
    
    # Padron distrito
    path('padron_situacion/get_distritos_padron/<int:distritos_id>/', get_distritos_padron, name='get_distritos_padron'),

    path('padron_situacion/p_distritos/', p_distritos_padron, name='p_distritos_padron'),
    #-- distrito excel
    path('rpt_distrito_padron/', RptDistritoPadron.as_view(), name = 'rpt_dist_padron_xls'),
    ####################################
    ### ACTAS DE HOMOLOGACION
    ####################################
    # Actas de Homologacion 
    path('actas_homologacion/', views.acta_index, name='actas_homologacion'),   
    
    ####################################
    ### COMPRISO 1 INDICADOR 1.1
    ####################################
    # Actas de Homologacion 
    path('compromiso/', views.compromiso_index, name='compromiso'),   
]