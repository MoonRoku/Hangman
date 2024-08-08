from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import *

class IndexView(View):
    def RegistrarUsuario(self, request, *args, **kwargs):
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            senha = form.cleaned_data.get('senha')
            
            usuario_existente = Usuario.objects.filter(nome=nome).exists()
            senha_correta = Usuario.objects.filter(nome=nome, senha=senha).exists()
            
            if usuario_existente and senha_correta:
                return redirect('index')
            elif not usuario_existente:
                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Senha incorreta!')
        else:
            messages.error(request, 'Formulário inválido!')
        
        return render(request, 'index.html', {'form': form})