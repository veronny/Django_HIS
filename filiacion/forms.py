from django.forms import ModelForm
from .models import Filiacion, Directorio, DirectorioRed, DirectorioEstablecimiento,TipoReporte, Diresa, Red, Microred, Establecimiento
from django import forms

class FiliacionForm(forms.ModelForm):
    class Meta:
       model =  Filiacion       
       fields = [
                 'provincia',
                 'distrito',
                 'tipo_municipalidad',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'provincia' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'distrito' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'tipo_municipalidad' : forms.Select(attrs={'class': 'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }

class DirectorioForm(forms.ModelForm):
    class Meta:
       model =  Directorio       
       fields = [
                 'diresa',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'diresa' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }
       
class DirectorioRedForm(forms.ModelForm):
    class Meta:
       model =  DirectorioRed    
       fields = [
                 'red',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'red' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }

class DirectorioEstablecimientoForm(forms.ModelForm):
    class Meta:
       model =  DirectorioEstablecimiento   
       fields = [
                 'red',
                 'microred',
                 'establecimiento',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'red' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'microred' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'establecimiento' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }
       
# forms.py reporte
class ReporteForm(forms.Form):
    tipo_reporte = forms.ModelChoiceField(queryset=TipoReporte.objects.all(), empty_label=None)
    diresa = forms.ModelChoiceField(queryset=Diresa.objects.all(), required=False)
    red = forms.ModelChoiceField(queryset=Red.objects.all(), required=False)
    microred = forms.ModelChoiceField(queryset=Microred.objects.all(), required=False)
    establecimiento = forms.ModelChoiceField(queryset=Establecimiento.objects.all(), required=False)
    
class FrmDiresa(forms.Form):
    diresa = forms.ModelChoiceField(queryset=Diresa.objects.all(), required=False)
class FrmRed(forms.ModelForm):
    class Meta:
        model = Red
        fields = ['nombre_red']
        widgets = {
                'nombre_red' : forms.TextInput(attrs={'class':'form-control'}),
        }
class FrmMicrored(forms.ModelForm):
    class Meta:
        model = Microred
        fields = ['nombre_microred', 'cod_red']
        widgets = {
                'nombre_microred' : forms.TextInput(attrs={'class':'form-control'}),
        }

class FrmEstablecimiento(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ['nombre_establecimiento', 'cod_red', 'cod_microred']
        widgets = {
                'nombre_establecimiento' : forms.TextInput(attrs={'class':'form-control'}),
        }