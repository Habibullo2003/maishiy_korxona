from django import forms
from .models import Korxona

class KorxonaForm(forms.ModelForm):
    class Meta:
        model = Korxona
        fields = '__all__'
        widgets = {
            'ochilgan_sana': forms.DateInput(attrs={'type': 'date'}),
            'qayta_ishlaydigan_materiallar': forms.Textarea(attrs={'rows': 3}),
            'izoh': forms.Textarea(attrs={'rows': 2}),
        }
