from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from filiacion import views 
# Subir archivos estaticos
from django.conf.urls.static import static
# Reporte excel
from filiacion.views import home, ReportePersonalizadoExcel, RptVistaDisExcel, RptSeguimientoVistaDisExcel, RptDiscapacidad2,FrmRedView
# Formularios
from filiacion.views import FrmMicroredView,FrmEstablecimientoView,form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    # directorio gobierno local
    path('filiacion/', views.filiacion, name='filiacion'),
    path('filiacion/create/', views.create_filiacion, name='create_filiacion'),
    path('filiacion/<int:filiacion_id>/', views.filiacion_detail, name='filiacion_detail'),
    path('filiacion/<int:filiacion_id>/delete', views.delete_filiacion, name='delete_filiacion'),
    # directorio salud DIRESA
    path('directorio_salud/', views.directorio_diresa, name='directorio_salud'),
    path('directorio/create/', views.create_directorio_diresa, name='create_directorio_diresa'),
    path('directorio/<int:directorio_diresa_id>/', views.directorio_diresa_detail, name='directorio_diresa_detail'),
    path('create_directorio/<int:directorio_salud_id>/delete', views.delete_directorio_diresa, name='delete_directorio_diresa'),
    # directorio salud RED
    path('directorio_red/', views.directorio_red, name='directorio_red'),
    path('directorio_red/create/', views.create_directorio_red, name='create_directorio_red'),
    path('directorio_red/<int:directorio_red_id>/', views.directorio_red_detail, name='directorio_red_detail'),
    # directorio salud ESTABLECIMIENTO
    path('directorio_establecimiento/', views.directorio_establecimiento, name='directorio_establecimiento'),
    path('directorio_establecimiento/create/', views.create_directorio_establecimiento, name='create_directorio_establecimiento'),
    path('directorio_establecimiento/<int:directorio_establecimiento_id>/', views.directorio_establecimiento_detail, name='directorio_establecimiento_detail'),
    #frontend routes
    path('frontend_filiacion/', views.frontend_filiacion, name='frontend_filiacion'),
    path('frontend_directorio_diresa/', views.frontend_directorio_diresa, name='frontend_directorio_diresa'),
    path('frontend_directorio_red/', views.frontend_directorio_red, name='frontend_directorio_red'),
    path('frontend_directorio_establecimiento/', views.frontend_directorio_establecimiento, name='frontend_directorio_establecimiento'),
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
    path('tipo_reporte/', views.TipoReporte, name='tipo_reporte'),
    path('rpt_operacional_dis/', RptDiscapacidad2.as_view(), name='rpt_operacional_dis'),
    
    path('frm_red/', FrmRedView.as_view(), name='frm_red'),
    path('frm_microred/', FrmMicroredView.as_view(), name='frm_microred'),
    path('frm_establecimiento/', FrmEstablecimientoView.as_view(), name='frm_establecimiento'),
    
    path('form/<str:form_type>/', form_view, name='form_view'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)