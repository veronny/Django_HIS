from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from filiacion import views 
# Subir archivos estaticos
from django.conf.urls.static import static
# Reporte excel
from filiacion.views import home, ReportePersonalizadoExcel, RptVistaDisExcel, RptSeguimientoVistaDisExcel, RptDiscapacidad2
# Formularios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    #################################################################################
    ######## MODULO DE DISCAPACIDAD #################################################
    #################################################################################
    path('rpt_discapacidad/', views.listar_rpt_discapacidad, name='rpt_discapacidad'),
    path('reporte/', ReportePersonalizadoExcel.as_view(), name = 'reporte'),
    # VISITAS DISCAPACIDAD
    path('rpt_visita_dis/', views.listar_rpt_visita_dis, name='rpt_visita_dis'),
    path('reporte_visita_dis/', RptVistaDisExcel.as_view(), name = 'reporte_visita_dis'),
    # SEGUIMIENTO VISITAS DISCAPACIDAD
    path('rpt_seguimiento_visita_dis/', views.listar_rpt_seguimiento_visita_dis, name='rpt_seguimiento_visita_dis'),
    path('reporte_seguimiento_visita_dis/', RptSeguimientoVistaDisExcel.as_view(), name = 'reporte_seguimiento_visita_dis'),
    # OPERACIONAL DISCAPACIDAD
    path('rpt_operacional_dis/', views.TipoReporte, name='rpt_operacional_dis'),
    path('rpt_operacional_dis/', RptDiscapacidad2.as_view(), name='rpt_operacional_dis'),
          
        
    # PADRON NOMINAL
    path('', include('filiacion.urls'))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)