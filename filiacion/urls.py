# miapp/urls.py
from django.urls import path
from .views import index, get_distritos, p_distritos, get_redes, get_provincias, get_microredes, p_microredes, p_microredes_principal
from .views import get_establecimientos,p_establecimientos, get_chart, get_chart_ranking
from .views import RptProvinciaVistaExcel, RptDistritoVistaExcel, RptRedVistaExcel, RptMicroredVistaExcel, RptEstablecimientoVistaExcel

app_name = 'filiacion'

urlpatterns = [
    
    ## Padron Nominal
    path('padron/', index, name='padron_index'),
    # provincia
    path('get_provincias/<int:provincias_id>/', get_provincias, name='get_provincias'),
    #-- provincia excel
    path('rpt_seguimiento_visita_excel/', RptProvinciaVistaExcel.as_view(), name = 'rpt_seg_visita_xls'),
    
    # distrito
    path('get_distritos/<int:distritos_id>/', get_distritos, name='get_distritos'),
    path('p_distritos/', p_distritos, name='p_distritos'),
    #-- distrito excel
    path('rpt_seg_visita_distrito/', RptDistritoVistaExcel.as_view(), name = 'rpt_seg_visita_distrito'),
    
    # redes
    path('get_redes/<int:redes_id>/', get_redes, name='get_redes'),
    #-- redes excel
    path('rpt_seg_visita_red/', RptRedVistaExcel.as_view(), name = 'rpt_seg_visita_red'),
    
    # microred
    path('get_microredes/<int:microredes_id>/', get_microredes, name='get_microredes'),
    path('p_microredes_principal/', p_microredes_principal, name='p_microredes_principal'),
    path('p_microredes/', p_microredes, name='p_microredes'),
    #-- microred excel
    path('rpt_seg_visita_microred/', RptMicroredVistaExcel.as_view(), name = 'rpt_seg_visita_microred'),
    
    # establecimientos
    path('get_establecimientos/<int:establecimiento_id>/', get_establecimientos, name='get_establecimientos'),
    path('p_establecimiento/', p_establecimientos, name='p_establecimientos'),
    #-- establecimiento excel
    path('rpt_seg_visita_establecimiento/', RptEstablecimientoVistaExcel.as_view(), name = 'rpt_seg_visita_establecimiento'),
       
    # graficos
    path('get_chart/', get_chart, name='get_chart'),
    path('get_chart_ranking/', get_chart_ranking, name='get_chart_ranking')
    
    # SEGUIMIENTO VISITAS 
    #path('rpt_seguimiento_visita_dis/', views.listar_rpt_seguimiento_visita_dis, name='rpt_seguimiento_visita_dis'),
    #path('reporte_seguimiento_visita_dis/', RptSeguimientoVistaDisExcel.as_view(), name = 'reporte_seguimiento_visita_dis'),
    
]