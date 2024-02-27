from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import Padron

# report excel
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

# tablas por redes
from django.db.models import Sum, F, FloatField, ExpressionWrapper,Count, Value, Q
from django.db.models.functions import Cast, Round,Coalesce 
################################################
# SITUACION PADRON NOMINAL - VISITA DOMICILARIO
################################################
@login_required
def index(request):
    p_chyo = 'CHANCHAMAYO'
    p_chupaca = 'CHUPACA'
    p_concepcion = 'CONCEPCION'
    p_huancayo = 'HUANCAYO'
    p_jauja = 'JAUJA'
    p_junin = 'JUNIN'
    p_satipo = 'SATIPO'
    p_tarma = 'TARMA'
    p_yauli = 'YAULI'
       
    t_chyo = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_chyo).order_by('distrito')                                                                                   

    t_chupaca = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_chupaca).order_by('distrito')                                          
    
    t_concepcion = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_concepcion).order_by('distrito')                                                        
    
    t_huancayo = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_huancayo).order_by('distrito')      
    
    t_jauja = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_jauja).order_by('distrito')      
    
    t_junin = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_junin).order_by('distrito') 
    
    t_satipo = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_satipo).order_by('distrito')        
    
    t_tarma = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_tarma).order_by('distrito')  
    
    t_yauli = Padron.objects.values('distrito').annotate( 
                                                        sum_0_28d =Sum('edad_0_28_dias'),
                                                        sum_0_5m =Sum('edad_0_5_meses'),
                                                        sum_6_11m=Sum('edad_6_11_meses'),
                                                        sum_12m=Sum('menores_de_12_meses'),
                                                        sum_1a=Sum('edad_1_anio'),
                                                        sum_2a=Sum('edad_2_anios'),
                                                        sum_3a=Sum('edad_3_anios'),
                                                        sum_4a=Sum('edad_4_anios'),
                                                        sum_5a=Sum('edad_5_anios'),
                                                        sum_num = Count('num_num_doc', filter=Q(num_num_doc=0)),
                                                        sum_seguro= Count('num_seguro',filter=Q(num_seguro=0)),
                                                        sum_enc= Count('num_enc', filter=Q(num_enc=0)),
                                                        sum_vis= Count('num_vis', filter=Q(num_vis=0)),
                                                        sum_num_cel= Count('num_num_cel', filter=Q(num_num_cel=0)),
                                                        sum_frecuencia= Count('num_frecuencia', filter=Q(num_frecuencia=0)),
                                                        sum_entidad= Count('num_entidad_reniec', filter=Q(num_entidad_reniec=0)),
                                                        ).filter(provincia=p_yauli).order_by('distrito')  
    
    context = {
                't_chyo'      : t_chyo,
                't_chupaca'   : t_chupaca,
                't_concepcion': t_concepcion,
                't_huancayo'  : t_huancayo,
                't_jauja'     : t_jauja,
                't_junin'     : t_junin,
                't_satipo'    : t_satipo,
                't_tarma'     : t_tarma,
                't_yauli'     : t_yauli,
              }
    
    return render(request, 'situacion.html', context)

#####################################################################
#---  GRAFICOS PRINCIPAL CANTIDAD DE NIÑOS ---------------------------
def get_chart_padron_edades(_request):
    # Consulta para obtener los datos de ventas
    
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie=['1446','9275','10063','19338','20874','21079','23129','24515','24554']
   
    chart_padron_edades = {
        'tooltip':{
            'show': True,
            'trigger': "axis",
            'triggerOn': "mousemove|click"    
        },
        'legend':{# Nombre para la leyenda
        },       
        'xAxis':[
            {
                'type':"category",
                'data':["0 a 28 d","0 a 5 meses","6 a 11 meses","> de 1 año","1 años","2 años","3 años","4 años","5 años"]
            }            
        ],
        'yAxis':[
            {
                'type':"value",
                'axisLine': {
                        'lineStyle': {
                            'color': colors[0]
                        }
                },
            }            
        ],
        'series':[
            {
                'name': 'Cantidad',
                'data': serie,
                'type': "bar",
            }, 
        ], 
    }
    
    return JsonResponse(chart_padron_edades)

#---  PORCENTAJE DE NIÑO SEXO ------------------------------------------------
def get_chart_padron_sexo(_request):
    # Consulta para obtener los datos de ventas
    
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4000']
    serie2 = ['3001']
   
    chart_padron_sexo = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '5%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : '% de niños sin DNI',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Masculino'
                        },
                        { 
                         'value': serie2,
                         'name': 'Femenino' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_sexo)

#---  PORCENTAJE DE NIÑO DNI ------------------------------------------------
def get_chart_padron_dni(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['2700']
    serie2 = ['130789']
   
    chart_padron_dni = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin DNI'
                        },
                        { 
                         'value': serie2,
                         'name': 'Con DNI' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_dni)

#---  PORCENTAJE DE NIÑO SIN SEGURO ------------------------------------------------
def get_chart_padron_seguro(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_seguro = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin Seguro'
                        },
                        { 
                         'value': serie2,
                         'name': 'Con Seguro' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_seguro)

#---  PORCENTAJE DE NIÑO ENCONTRADO ------------------------------------------------
def get_chart_padron_encontrado(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_encontrado = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'No Encontrado'
                        },
                        { 
                         'value': serie2,
                         'name': 'Encontrado' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_encontrado)

#---  PORCENTAJE DE NIÑO VISITADO ------------------------------------------------
def get_chart_padron_visitado(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_visitado = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin Visita'
                        },
                        { 
                         'value': serie2,
                         'name': 'Visitado' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_visitado)

#---  PORCENTAJE DE CELULAR MAMA  ------------------------------------------------
def get_chart_padron_celular(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_celular = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin Celular Madre'
                        },
                        { 
                         'value': serie2,
                         'name': 'Celular Madre' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_celular)

#---  PORCENTAJE DE CELULAR MAMA  ------------------------------------------------
def get_chart_padron_frecuencia(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_frecuencia = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin Celular Madre'
                        },
                        { 
                         'value': serie2,
                         'name': 'Celular Madre' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_frecuencia)


#---  PORCENTAJE DE ENTIDAD  ------------------------------------------------
def get_chart_padron_entidad(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['9151']
    serie3 = ['3151']
   
    chart_padron_entidad = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Municipio'
                        },
                        { 
                         'value': serie2,
                         'name': 'EESS SALUD' 
                        },
                                                { 
                         'value': serie3,
                         'name': 'RENIEC' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_entidad)

#---  PORCENTAJE DE AVANCE HIS MINSA ------------------------------------------------
def get_chart_padron_atencion(_request):
    # Consulta para obtener los datos de ventas   
    # Formatear los datos para pasarlos a la plantilla
    colors = ['#5470C6', '#91CC75', '#EE6666'];   
    
    serie1 = ['4338']
    serie2 = ['129151']
   
    chart_padron_atencion = {
        'tooltip':{
            'trigger': "item",
        },
        'legend':{
            'top': '2%',
            'left': 'center'# Nombre para la leyenda
        },       
        'series':[
            {
             'name'  : 'Cant niños ',
             'type'  : 'pie',
             'radius': ['40%', '70%'],
             'avoidLabelOverlap': 'false',
             'itemStyle': {
                    'borderRadius': 10,
                    'borderColor': '#fff',
                    'borderWidth': 2
            },
             'label': {
                'show': 'false',
                'position': 'center'
             },
             'emphasis': {
                 'label': {
                 'show': 'true',
                 'fontSize': 40,
                 'fontWeight': 'bold'
               }
             },
             'labelLine': {
               'show': 'false'
             },
             'data': [
                        { 
                         'value': serie1,
                         'name' : 'Sin HIS MINSA'
                        },
                        { 
                         'value': serie2,
                         'name': 'HIS MINSA' 
                        },
                    ]
            }     
        ] 
    };
    
    return JsonResponse(chart_padron_atencion)

