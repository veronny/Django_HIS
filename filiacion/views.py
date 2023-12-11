from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

# Create your views here.
from .forms import FiliacionForm, DirectorioForm, DirectorioRedForm, DirectorioEstablecimientoForm, ReporteForm, FrmDiresa, FrmRed, FrmMicrored, FrmEstablecimiento
from .models import Filiacion, Directorio, DirectorioRed, DirectorioEstablecimiento, Diresa, Provincia, Distrito, Red, Microred, Establecimiento 
from .models import rpt_certificado, ActualizaBD,RptVisitaDis,RptSeguimientoVisitaDis, TipoReporte

# report excel
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill,Side

# report operacionales
from django.db import models
from django.db import connection
from django.views import View

def home(request):
    actualiza = ActualizaBD.objects.all()
    context = {
                'actualiza': actualiza,
                }    
    return render(request, 'home.html', context)

# ----- DIRECTORIO MUNICIPIO --------------------
@login_required
def filiacion(request):
    filiaciones = Filiacion.objects.all()
    context = {
                'filiaciones': filiaciones,
                }
    return render(request, 'filiacion.html', context)

@login_required
def create_filiacion(request):
    if request.method == "GET":
        return render(request, 'create_filiacion.html', {
            "form": FiliacionForm
        })
    else:
        try:
            form = FiliacionForm(request.POST, request.FILES)
            new_filiacion = form.save(commit=False)
            new_filiacion.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'create_filiacion.html', {
                "form": FiliacionForm,
                "error": "Error creating task."
            })

@login_required
def filiacion_detail(request, filiacion_id):
    if request.method == 'GET':
        filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
        form = FiliacionForm(instance=filiacion)
        context = {
            'filiacion': filiacion,
            'form': form
        }
        return render(request, 'filiacion_detail.html', context)
    else:
        try:
            filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
            form = FiliacionForm(request.POST,request.FILES, instance=filiacion)
            form.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'filiacion_detail.html', {'filiacion': filiacion, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_filiacion(request, filiacion_id):
    filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
    if request.method == 'POST':
        filiacion.delete()
        return redirect('filiacion')

# ----- DIRECTORIO SALUD DIRESA --------------------
@login_required
def directorio_diresa(request):
    directorio_diresas = Directorio.objects.all()
    context = {
                'directorio_diresas': directorio_diresas,
                }
    return render(request, 'directorio_diresa.html', context)

@login_required
def create_directorio_diresa(request):
    if request.method == "GET":
        return render(request, 'create_directorio_diresa.html', {
            "form": DirectorioForm
        })
    else:
        try:
            form = DirectorioForm(request.POST, request.FILES)
            new_directorio = form.save(commit=False)
            new_directorio.save()
            return redirect('directorio_salud')
        except ValueError:
            return render(request, 'create_directorio_diresa.html', {
                "form": DirectorioForm,
                "error": "Error creating task."
            })

@login_required
def directorio_diresa_detail(request, directorio_diresa_id):
    if request.method == 'GET':
        directorio_diresa = get_object_or_404(Directorio, pk=directorio_diresa_id)
        form = DirectorioForm(instance=directorio_diresa)
        context = {
            'directorio_diresa': directorio_diresa,
            'form': form
        }
        return render(request, 'directorio_diresa_detail.html', context)
    else:
        try:
            directorio_diresa = get_object_or_404(Directorio, pk=directorio_diresa_id)
            form = DirectorioForm(request.POST,request.FILES, instance=directorio_diresa)
            form.save()
            return redirect('directorio_salud')
        except ValueError:
            return render(request, 'directorio_diresa_detail.html', {'directorio_diresa': directorio_diresa, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_directorio_diresa(request, directorio_diresa_id):
    directorio = get_object_or_404(Directorio, pk=directorio_diresa_id)
    if request.method == 'POST':
        directorio.delete()
        return redirect('directorio_salud')

# ----- DIRECTORIO SALUD RED --------------------
@login_required
def directorio_red(request):
    directorio_redes = DirectorioRed.objects.all()
    context = {
                'directorio_redes': directorio_redes,
                }
    return render(request, 'directorio_red.html', context)

@login_required
def create_directorio_red(request):
    if request.method == "GET":
        return render(request, 'create_directorio_red.html', {
            "form": DirectorioRedForm
        })
    else:
        try:
            form = DirectorioRedForm(request.POST, request.FILES)
            new_directorio_red = form.save(commit=False)
            new_directorio_red.save()
            return redirect('directorio_red')
        except ValueError:
            return render(request, 'create_directorio_red.html', {
                "form": DirectorioRedForm,
                "error": "Error creating task."
            })

@login_required
def directorio_red_detail(request, directorio_red_id):
    if request.method == 'GET':
        directorio_red = get_object_or_404(DirectorioRed, pk=directorio_red_id)
        form = DirectorioRedForm(instance=directorio_red)
        context = {
            'directorio_red': directorio_red,
            'form': form
        }
        return render(request, 'directorio_red_detail.html', context)
    else:
        try:
            directorio_red = get_object_or_404(DirectorioRed, pk=directorio_red_id)
            form = DirectorioRedForm(request.POST,request.FILES, instance=directorio_red)
            form.save()
            return redirect('directorio_red')
        except ValueError:
            return render(request, 'directorio_red_detail.html', {'directorio_red': directorio_red, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_directorio_red(request, directorio_red_id):
    directorio_red = get_object_or_404(DirectorioRed, pk=directorio_red_id)
    if request.method == 'POST':
        directorio_red.delete()
        return redirect('directorio_red')

# ----- DIRECTORIO SALUD ESTABLECIMIENTO --------------------
@login_required
def directorio_establecimiento(request):
    directorio_establecimientos = DirectorioEstablecimiento.objects.all()
    context = {
                'directorio_establecimientos': directorio_establecimientos,
                }
    return render(request, 'directorio_establecimiento.html', context)

@login_required
def create_directorio_establecimiento(request):
    if request.method == "GET":
        return render(request, 'create_directorio_establecimiento.html', {
            "form": DirectorioEstablecimientoForm
        })
    else:
        try:
            form = DirectorioEstablecimientoForm(request.POST, request.FILES)
            new_directorio_establecimiento = form.save(commit=False)
            new_directorio_establecimiento.save()
            return redirect('directorio_establecimiento')
        except ValueError:
            return render(request, 'create_directorio_establecimiento.html', {
                "form": DirectorioEstablecimientoForm,
                "error": "Error creating task."
            })

@login_required
def directorio_establecimiento_detail(request, directorio_establecimiento_id):
    if request.method == 'GET':
        directorio_establecimiento = get_object_or_404(DirectorioEstablecimiento, pk=directorio_establecimiento_id)
        form = DirectorioEstablecimientoForm(instance=directorio_establecimiento)
        context = {
            'directorio_establecimiento': directorio_establecimiento,
            'form': form
        }
        return render(request, 'directorio_establecimiento_detail.html', context)
    else:
        try:
            directorio_establecimiento = get_object_or_404(DirectorioEstablecimiento, pk=directorio_establecimiento_id)
            form = DirectorioEstablecimientoForm(request.POST,request.FILES, instance=directorio_establecimiento)
            form.save()
            return redirect('directorio_establecimiento')
        except ValueError:
            return render(request, 'directorio_establecimiento_detail.html', {'directorio_establecimiento': directorio_establecimiento, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_directorio_establecimiento(request, directorio_establecimiento_id):
    directorio_establecimiento = get_object_or_404(DirectorioEstablecimiento, pk=directorio_establecimiento_id)
    if request.method == 'POST':
        directorio_establecimiento.delete()
        return redirect('directorio_establecimiento')

# ----- INICIO DE SESION --------------------------------
@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password fo not match'
        })

# ----- SELECT DEPENDIENTES FILIACION --------------------
def distrito(request):
    provincias = request.GET.get('provincia_selected')
    distritos = Distrito.objects.filter(provincia_id=provincias)
    context = {
                'distritos': distritos, 
                'is_htmx': True 
                }
    return render(request, 'partials/distritos.html', context)

# ----- FRONTEND FILIACION --------------------
def frontend_filiacion(request):
    filiaciones = Filiacion.objects.all()
    context = {
            'filiaciones': filiaciones,
            }
    return render(request, 'frontend/filiacion.html', context)

def frontend_directorio_diresa(request):
    directorio_diresas= Directorio.objects.all()
    context = {
            'directorio_diresas': directorio_diresas,
            }
    return render(request, 'frontend/directorio_diresa.html', context)

def frontend_directorio_red(request):
    directorio_redes= DirectorioRed.objects.all()
    context = {
            'directorio_redes': directorio_redes,
            }
    return render(request, 'frontend/directorio_red.html', context)

def frontend_directorio_establecimiento(request):
    directorio_establecimientos= DirectorioEstablecimiento.objects.all()
    context = {
            'directorio_establecimientos': directorio_establecimientos,
            }
    return render(request, 'frontend/directorio_establecimiento.html', context)

#############################################
# ----- RPT DISCAPACIDAD --------------------
#############################################
@login_required
def listar_rpt_discapacidad(request):
    
    # Obtener el filtro de mes y año del parámetro GET
    # Obtener todas las marcaciones o filtrar por mes/año
    return render(request, 'rpt_discapacidad/rpt_discapacidad.html')

class ReportePersonalizadoExcel(TemplateView):
    def get(self,request,*args,**kwargs):
        # creacion de la consulta
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        query = rpt_certificado.objects.filter(Fecha_Atencion__range=[fecha_inicio, fecha_fin]).order_by('Red','MicroRed','Nombre_Establecimiento')

        # creacion de archivo
        wb = Workbook() #crea libro de trabajo
        ws = wb.active #Primera hoja

        # crea titulo del reporte
        ws['A1'].alignment = Alignment(horizontal= "center", vertical="center")
        ws['A1'].font = Font(name = 'Arial', size= 14, bold = True)
        ws['A1'] = 'REPORTE DE CERTIFICADOS DE DISCAPACIDAD'
        # cambina celdas
        ws.merge_cells('A1:K1')

        ws['B3'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B3'].font = Font(name = 'Arial', size= 8)
        ws['B3'] = 'Fecha Inicio'
        
        ws['C3'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C3'].font = Font(name = 'Arial', size= 8)
        ws['C3'].value = fecha_inicio
    
        ws['B4'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B4'].font = Font(name = 'Arial', size= 8)
        ws['B4'] = 'Fecha Fin'
        
        ws['C4'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C4'].font = Font(name = 'Arial', size= 8)
        ws['C4'].number_format = "dd-mm-yyyy"
        ws['C4'].value = fecha_fin
        
        # cambia el alto de la columna
        ws.row_dimensions[1].height = 25
        # cambia el ancho de la columna
        ws.column_dimensions['B'].width = 23
        ws.column_dimensions['C'].width = 25
        ws.column_dimensions['D'].width = 14
        ws.column_dimensions['E'].width = 32
        ws.column_dimensions['F'].width = 12
        ws.column_dimensions['G'].width = 12
        ws.column_dimensions['H'].width = 10
        ws.column_dimensions['I'].width = 10
        ws.column_dimensions['J'].width = 10
        ws.column_dimensions['K'].width = 10
        # linea de division
        ws.freeze_panes = 'AL8'

        # crea cabecera
        # celda red 
        ws['B6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['B6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['B6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['B6'] = 'RED'
        ws.merge_cells('B6:B7')
        # celda microred 
        ws['C6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['C6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['C6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['C6'] = 'MICRORED'
        ws.merge_cells('C6:C7')
        # celda establecimiento
        ws['D6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['D6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['D6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['D6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['D6'] = 'COD ESTABLEC'
        ws.merge_cells('D6:D7')
        # celda codigo de establecimiento
        ws['E6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['E6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['E6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['E6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['E6'] = 'NOMBRE ESTABLECIMIENTO'
        ws.merge_cells('E6:E7')

        # celda codigo de establecimiento
        ws['F6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['F6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['F6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['F6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['F6'] = 'EVALUACION'
        ws.merge_cells('F6:F7')
        # celda codigo de establecimiento
        ws['G6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['G6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['G6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['G6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['G6'] = 'CALIFICACION'
        ws.merge_cells('G6:G7')
        # celda TITULO
        ws['H6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['H6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['H6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['H6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['H6'] = 'CERTIFICACION'
        ws.merge_cells('H6:K6')
        # celda 
        ws['H7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['H7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['H7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['H7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['H7'] = 'LEVE'
        # celda 
        ws['I7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['I7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['I7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['I7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['I7'] = 'MODERADO'
        # celda 
        ws['J7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['J7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['J7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['J7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['J7'] = 'SEVERO'
        # celda 
        ws['K7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['K7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['K7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['K7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['K7'] = 'S/GRADO'

        # Pintamos los datos del reporte - RED
        cont = 8       
        for q in query:   
            ws.cell(row = cont , column=2).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=2).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=2).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=2).value = q.Red

            ws.cell(row = cont , column=3).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=3).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=3).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=3).value = q.MicroRed
            
            ws.cell(row = cont , column=4).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=4).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=4).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 4).value = q.Codigo_Unico
            
            ws.cell(row = cont , column=5).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=5).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=5).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 5).value = q.Nombre_Establecimiento
            
            ws.cell(row = cont , column=6).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=6).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=6).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 6).value = q.DIS_EVALUACION
            
            ws.cell(row = cont , column=7).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=7).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=7).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 7).value = q.DIS_CALIFICACION
            
            ws.cell(row = cont , column=8).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=8).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=8).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 8).value = q.DIS_LEV
            
            ws.cell(row = cont , column=9).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=9).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=9).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 9).value = q.DIS_MOD
            
            ws.cell(row = cont , column=10).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=10).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=10).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 10).value = q.DIS_SEV
            
            ws.cell(row = cont , column=11).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=11).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=11).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 11).value = q.DIS_TOTAL            
            cont+=1

                
        #Respuesta de Django
        #Establecer el nombre del archivo
        nombre_archivo = "rpt_discapacidad.xlsx"
        #Definir el tipo de respuesta que se va a dar
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response

#############################################
# ----- RPT VISITA  --------------------
#############################################
@login_required
def listar_rpt_visita_dis(request):
    
    # Obtener el filtro de mes y año del parámetro GET
    # Obtener todas las marcaciones o filtrar por mes/año
    return render(request, 'rpt_discapacidad/rpt_visita_dis.html')

class RptVistaDisExcel(TemplateView):
    def get(self,request,*args,**kwargs):
        # creacion de la consulta
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        query = RptVisitaDis.objects.filter(Fecha_Atencion__range=[fecha_inicio, fecha_fin]).order_by('Red','MicroRed','Nombre_Establecimiento')

        # creacion de archivo
        wb = Workbook() #crea libro de trabajo
        ws = wb.active #Primera hoja

        # crea titulo del reporte
        ws['A1'].alignment = Alignment(horizontal= "center", vertical="center")
        ws['A1'].font = Font(name = 'Arial', size= 14, bold = True)
        ws['A1'] = 'REPORTE DE VISITA DOMICILIARIA A PACIENTES CON DISCAPACIDAD'
        # cambina celdas
        ws.merge_cells('A1:J1')

        ws['B3'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B3'].font = Font(name = 'Arial', size= 8)
        ws['B3'] = 'Fecha Inicio'
        
        ws['C3'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C3'].font = Font(name = 'Arial', size= 8)
        ws['C3'].value = fecha_inicio
    
        ws['B4'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B4'].font = Font(name = 'Arial', size= 8)
        ws['B4'] = 'Fecha Fin'
        
        ws['C4'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C4'].font = Font(name = 'Arial', size= 8)
        ws['C4'].number_format = "dd-mm-yyyy"
        ws['C4'].value = fecha_fin
        
        # cambia el alto de la columna
        ws.row_dimensions[1].height = 25
        # cambia el ancho de la columna
        ws.column_dimensions['B'].width = 23
        ws.column_dimensions['C'].width = 25
        ws.column_dimensions['D'].width = 14
        ws.column_dimensions['E'].width = 32
        ws.column_dimensions['F'].width = 10
        ws.column_dimensions['G'].width = 10
        ws.column_dimensions['H'].width = 10
        ws.column_dimensions['I'].width = 10
        # linea de division
        ws.freeze_panes = 'AL8'

        # crea cabecera
        ws['B6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['B6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['B6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['B6'] = 'RED'
        ws.merge_cells('B6:B7')

        ws['C6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['C6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['C6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['C6'] = 'MICRORED'
        ws.merge_cells('C6:C7')

        ws['D6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['D6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['D6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['D6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['D6'] = 'COD ESTABLEC'
        ws.merge_cells('D6:D7')

        ws['E6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['E6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['E6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['E6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['E6'] = 'NOMBRE ESTABLECIMIENTO'
        ws.merge_cells('E6:E7')

        ws['F6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['F6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['F6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['F6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['F6'] = '1° VISITA'
        ws.merge_cells('F6:F7')

        ws['G6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['G6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['G6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['G6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['G6'] = '2° VISITA'
        ws.merge_cells('G6:G7')
        # celda 
        ws['H6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['H6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['H6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['H6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['H6'] = '3° VISITA'
        ws.merge_cells('H6:H7')
        # celda 
        ws['I6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['I6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['I6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['I6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['I6'] = '4° VISITA'
        ws.merge_cells('I6:I7')
        # celda 

        # Pintamos los datos del reporte - RED
        cont = 8       
        for q in query:   
            ws.cell(row = cont , column=2).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=2).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=2).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=2).value = q.Red

            ws.cell(row = cont , column=3).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=3).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=3).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=3).value = q.MicroRed
            
            ws.cell(row = cont , column=4).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=4).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=4).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 4).value = q.Codigo_Unico
            
            ws.cell(row = cont , column=5).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=5).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=5).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 5).value = q.Nombre_Establecimiento
            
            ws.cell(row = cont , column=6).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=6).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=6).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 6).value = q.VISITA_1
            
            ws.cell(row = cont , column=7).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=7).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=7).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 7).value = q.VISITA_2
            
            ws.cell(row = cont , column=8).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=8).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=8).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 8).value = q.VISITA_3
            
            ws.cell(row = cont , column=9).alignment = Alignment(horizontal="right")
            ws.cell(row = cont , column=9).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=9).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 9).value = q.VISITA_4
                     
            cont+=1

                
        #Respuesta de Django
        #Establecer el nombre del archivo
        nombre_archivo = "rpt_visita_dis.xlsx"
        #Definir el tipo de respuesta que se va a dar
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response

#############################################
# ----- RPT SEGUMIENTO VISITA  --------------
#############################################
@login_required
def listar_rpt_seguimiento_visita_dis(request):
    
    # Obtener el filtro de mes y año del parámetro GET
    # Obtener todas las marcaciones o filtrar por mes/año
    return render(request, 'rpt_discapacidad/rpt_seguimiento_visita_dis.html')

class RptSeguimientoVistaDisExcel(TemplateView):
    def get(self,request,*args,**kwargs):
        # creacion de la consulta
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        query = RptSeguimientoVisitaDis.objects.filter(FECHA_VISITA_1__range=[fecha_inicio, fecha_fin]).order_by('Red','MicroRed','Nombre_Establecimiento')

        # creacion de archivo
        wb = Workbook() #crea libro de trabajo
        ws = wb.active #Primera hoja

        # crea titulo del reporte
        ws['A1'].alignment = Alignment(horizontal= "center", vertical="center")
        ws['A1'].font = Font(name = 'Arial', size= 14, bold = True)
        ws['A1'] = 'REPORTE DE SEGUIMIENTO VISITA DOMICILIARIA A PACIENTES CON DISCAPACIDAD'
        # cambina celdas
        ws.merge_cells('A1:J1')

        ws['B3'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B3'].font = Font(name = 'Arial', size= 8)
        ws['B3'] = 'Fecha Inicio'
        
        ws['C3'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C3'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C3'].font = Font(name = 'Arial', size= 8)
        ws['C3'].value = fecha_inicio
    
        ws['B4'].alignment = Alignment(horizontal= "left", vertical= "center")
        ws['B4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B4'].font = Font(name = 'Arial', size= 8)
        ws['B4'] = 'Fecha Fin'
        
        ws['C4'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C4'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['C4'].font = Font(name = 'Arial', size= 8)
        ws['C4'].number_format = "dd-mm-yyyy"
        ws['C4'].value = fecha_fin
        
        # cambia el alto de la columna
        ws.row_dimensions[1].height = 25
        # cambia el ancho de la columna
        ws.column_dimensions['B'].width = 10
        ws.column_dimensions['C'].width = 10
        ws.column_dimensions['D'].width = 39
        ws.column_dimensions['E'].width = 10
        ws.column_dimensions['F'].width = 39
        ws.column_dimensions['G'].width = 10
        ws.column_dimensions['H'].width = 39
        ws.column_dimensions['I'].width = 10
        ws.column_dimensions['J'].width = 39
        # linea de division
        ws.freeze_panes = 'AL8'

        # crea cabecera
        ws['B6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['B6'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['B6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['B6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['B6'] = 'DNI'
        ws.merge_cells('B6:B7')

        ws['C6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['C6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['C6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['C6'] = '1° VISITA'
        ws.merge_cells('C6:D6')
        
        ws['C7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['C7'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['C7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['C7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['C7'] = 'FECHA'

        ws['D7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['D7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['D7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['D7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['D7'] = 'ESTABLECIMIENTO'
        ##
        ws['E6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['E6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['E6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['E6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['E6'] = '2° VISITA'
        ws.merge_cells('E6:F6')
        
        ws['E7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['E7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['E7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['E7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['E7'] = 'FECHA'


        ws['F7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['F7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['F7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['F7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['F7'] = 'ESTABLECIMIENTO'

        ws['G6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['G6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['G6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['G6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['G6'] = '3° VISITA'
        ws.merge_cells('G6:H6')
        
        ws['G7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['G7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['G7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['G7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['G7'] = 'FECHA'
        # celda 
        ws['H7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['H7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['H7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['H7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['H7'] = 'ESTABLECIMIENTO'
        # celda 
        ws['I6'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['I6'].border = Border(left = Side(border_style = "thin"), 
                                     right = Side(border_style = "thin"), 
                                     top = Side(border_style = "thin"), 
                                     bottom = Side(border_style = "thin"))
        ws['I6'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['I6'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['I6'] = '4° VISITA'
        ws.merge_cells('I6:J6')
        
        
        ws['I7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['I7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['I7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['I7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['I7'] = 'FECHA'
        # celda 
        ws['J7'].alignment = Alignment(horizontal= "center", vertical= "center")
        ws['J7'].border = Border(left = Side(border_style = "thin"), 
                                 right = Side(border_style = "thin"), 
                                 top = Side(border_style = "thin"), 
                                 bottom = Side(border_style = "thin"))
        ws['J7'].fill = PatternFill(start_color = 'DDF2FD', end_color='DDF2FD', fill_type="solid")
        ws['J7'].font = Font(name = 'Arial', size= 9, bold = True)
        ws['J7'] = 'ESTABLECIMIENTO'

        # Pintamos los datos del reporte - RED
        cont = 8       
        for q in query:   
            ws.cell(row = cont , column=2).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=2).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=2).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=2).value = q.Numero_Documento_Paciente

            ws.cell(row = cont , column=3).alignment = Alignment(horizontal="center")
            ws.cell(row = cont , column=3).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=3).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column=3).value = q.FECHA_VISITA_1
            
            ws.cell(row = cont , column=4).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=4).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=4).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 4).value = q.EESS_VISITA_1
            
            ws.cell(row = cont , column=5).alignment = Alignment(horizontal="center")
            ws.cell(row = cont , column=5).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=5).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 5).value = q.FECHA_VISITA_2
            
            ws.cell(row = cont , column=6).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=6).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=6).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 6).value = q.EESS_VISITA_2
            
            ws.cell(row = cont , column=7).alignment = Alignment(horizontal="center")
            ws.cell(row = cont , column=7).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=7).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 7).value = q.FECHA_VISITA_3
            
            ws.cell(row = cont , column=8).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=8).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=8).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 8).value = q.EESS_VISITA_3
            
            ws.cell(row = cont , column=9).alignment = Alignment(horizontal="center")
            ws.cell(row = cont , column=9).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=9).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 9).value = q.FECHA_VISITA_4
            
            ws.cell(row = cont , column=10).alignment = Alignment(horizontal="left")
            ws.cell(row = cont , column=10).border = Border(left = Side(border_style = "thin"), 
                                                                right = Side(border_style = "thin"), 
                                                                top = Side(border_style = "thin"), 
                                                                bottom = Side(border_style = "thin"))
            ws.cell(row = cont , column=10).font = Font(name = 'Calibri', size= 8)
            ws.cell(row = cont , column= 10).value = q.EESS_VISITA_4
            
            cont+=1

                
        #Respuesta de Django
        #Establecer el nombre del archivo
        nombre_archivo = "rpt_seguimiento_visita_dis.xlsx"
        #Definir el tipo de respuesta que se va a dar
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response

#############################################
# ----- RPT DISCAPACIDAD POSTGRES -----------
#############################################
class RptDiscapacidad2(View):
    def get(self, request):
        # Llamada a la función PostgreSQL
        results = self.get_results_from_postgres(2023,1,2,1,6,631)  # Puedes ajustar los valores según tus necesidades
      
        # Renderizar el template y pasar los resultados
        return render(request, 'rpt_discapacidad/rpt_operacional_dis.html', {'results': results})

    def get_results_from_postgres(self, anio, mes_inicio, mes_fin, cod_red, cod_microred, cod_establec):
        # Establecer una conexión a la base de datos    
        with connection.cursor() as cursor:
            # Ejecutar la función PostgreSQL
            cursor.execute(f"SELECT * FROM rpt_discapacidad2({anio}, {mes_inicio}, {mes_fin}, {cod_red}, {cod_microred}, {cod_establec})")         
            # Obtener los resultados
            results = cursor.fetchall()

        return results
    
    


@login_required
def TipoReporte(request):
    tipo_reporte = TipoReporte.objects.all()
    context = {
                'tipo_reporte': tipo_reporte,
                }
    print(context)
    return render(request, 'partials/tipo_reporte.html', context)

class FrmRedView(View):
    template_name = 'partials/frm_red.html'

    def get(self, request, *args, **kwargs):
        form_red = FrmRed()
        return render(request, self.template_name, {'form_red': form_red})

class FrmMicroredView(View):
    template_name = 'partials/frm_microred.html'

    def get(self, request, *args, **kwargs):
        form = FrmMicrored()
        return render(request, self.template_name, {'form': form})

class FrmEstablecimientoView(View):
    template_name = 'partials/frm_establecimiento.html'

    def get(self, request, *args, **kwargs):
        form = FrmEstablecimiento()
        return render(request, self.template_name, {'form': form})
   
def form_view(request, form_type):
    # Lógica para determinar el formulario según el tipo
    if form_type == 'red':
        # Lógica para el formulario de red
        pass
    elif form_type == 'microred':
        # Lógica para el formulario de microred
        pass
    elif form_type == 'establecimiento':
        # Lógica para el formulario de establecimiento
        pass

    return render(request, 'rpt_discapacidad/formulario2.html', {'form_type': form_type})