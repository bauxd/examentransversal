from django import forms

from django.forms import ModelForm

from .models import infocompra


class formcompra(ModelForm):
    class Meta:
        model =  infocompra
        fields = ['nombre','apellido','rut','direccion','producto','correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.Textarea(attrs={'class': 'form-control'}),
            }