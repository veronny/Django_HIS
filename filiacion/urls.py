# miapp/urls.py
from django.urls import path
from .views import index, get_distritos, p_distritos, get_redes, get_provincias, get_microredes, p_microredes, get_establecimientos, p_establecimientos

app_name = 'filiacion'

urlpatterns = [
    
    ## Padron Nominal
    path('padron/', index, name='padron_index'),
    # provincia
    path('get_provincias/<int:provincias_id>/', get_provincias, name='get_provincias'),
    # distrito
    path('get_distritos/<int:distritos_id>/', get_distritos, name='get_distritos'),
    path('p_distritos/', p_distritos, name='p_distritos'),
    # redes
    path('get_redes/<int:redes_id>/', get_redes, name='get_redes'),
    # microred
    path('get_microredes/<int:microredes_id>/', get_microredes, name='get_microredes'),
    path('p_microredes/', p_microredes, name='p_microredes'),
    # establecimientos
    path('get_establecimientos/<int:establecimiento_id>/', get_establecimientos, name='get_establecimientos'),
    path('p_establecimiento/', p_establecimientos, name='p_establecimientos'),
]