from django import forms
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nome', 'senha']
        
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogador', 'sequencia', 'tentativas_restantes']