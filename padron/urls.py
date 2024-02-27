from django.urls import path
from . import views

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
    path('padron_situacion/get_chart_padron_atencion/', views.get_chart_padron_atencion, name='get_chart_padron_atencion'),
]