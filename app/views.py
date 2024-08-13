from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import *

class IndexView(View):
    def get(self, request):
        form = CadastroForm()
        return render(request, 'index.html', {'form': form})
    
    def post(self, request):
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            
            senha = form.cleaned_data.get('senha')
            
            usuario_existente = Usuario.objects.filter(nome=nome).exists()
            senha_correta = Usuario.objects.filter(nome=nome, senha=senha).exists()
            
            if usuario_existente and senha_correta:
                request.session['nome'] = nome
                return redirect('jogo')
            elif not usuario_existente:
                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Senha incorreta!')
        else:
            messages.error(request, 'Formulário inválido!')
        
        return render(request, 'index.html', {'form': form})

class HangmanView(View):
    def get(self, request):
        nome = request.session.get('nome')
        
        palavra = Palavra.objects.order_by('?').first()
        dica = Palavra.dica
        
        
        return render(request, 'hangmangame.html', {'nome': nome, 'palavra': palavra, 'dica': dica})

    def post(self, request):
        return