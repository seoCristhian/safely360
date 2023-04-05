from django.forms import ModelForm
from django import forms
from .models import *

#class UsuarioForm(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['nombre', 'correo']

class UsuarioFormSafely(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus']=True
    
    class Meta:
        model=registroSafely
        fields='__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su Nombre', 'type':'text'}),
            'area': forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Área de trabajo(Electricidad, mecanica, etc)', 'type':'text'}),
            'correo': forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Ingrese su Correo Electrónico', 'type':'text'}),
        }
'''
class UsuarioFormsSafelyEmpresa(ModelForm):
    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus']= True
    
    class Meta:
        model = registroSafelyEmpresa
        fields = '__all__'
        widgets = {
            'celular' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su Nombre', 'type':'text'}),
            'empresa' : forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Ingrese su Correo', 'type':'text'}),
            'rubro' : forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Ingrese su Correo', 'type':'text'}),
        }

'''



