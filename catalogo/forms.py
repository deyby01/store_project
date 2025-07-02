from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['autor', 'texto', 'calificacion']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'calificacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }