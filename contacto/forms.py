from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', max_length=100,required=True)
    apellidos=forms.CharField(label='Apellidos', max_length=100,required=True)
    email=forms.CharField(label='Email', max_length=100,required=True)
    mensaje=forms.CharField(label='Mensaje', widget=forms.Textarea)
    