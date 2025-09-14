from django.forms import ModelForm
from .models import Tarea 
from django import forms  

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['title', 'description', 'important']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control' , 'placeholder': 'Describe la tarea...'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la tarea...'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})}