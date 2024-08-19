from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import *

class IndexView(View):
    def get(self, request):
        form = CadastroForm()
        rank = Jogo.objects.order_by('-sequencia')
        return render(request, 'index.html', {'form': form, 'rank': rank})
    
    def post(self, request):
        rank = Jogo.objects.order_by('-sequencia')
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
        
        return render(request, 'index.html', {'form': form, 'rank': rank})

class HangmanView(View):
    def get(self, request):
        nome = request.session.get('nome')
        form = JogoForm()
        
        palavra = Palavra.objects.order_by('?').first()
        dica = palavra.dica
        palavraP = palavra.palavra
        
        return render(request, 'hangmangame.html', {'form': form, 'nome': nome, 'palavra': palavra, 'dica': dica, 'palavraP': palavraP})

    def post(self, request):
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogo')
        
        return render(request, 'hangmangame.html', {'form': form})