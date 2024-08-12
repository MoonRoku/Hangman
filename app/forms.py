from django import forms
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nome', 'senha']
        
class PalavraForm(forms.ModelForm):
    class Meta:
        model = Palavra
        fields = ['palavra']