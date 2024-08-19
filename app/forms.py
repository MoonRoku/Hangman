from django import forms
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nome', 'senha']
        
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogador', 'sequencia']
    
    def __init__(self, *args, **kwargs):
        super(JogoForm, self).__init__(*args, **kwargs)
        self.fields['jogador'].widget.attrs.update({'class': 'texto'})
        self.fields['sequencia'].widget.attrs.update({'class': 'texto'})