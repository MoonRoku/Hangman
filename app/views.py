from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import *
import random

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
        palavra = Palavra.objects.order_by('?').first()
        if palavra:
            palavra_oculta = '_' * len(palavra.palavra)
            context = {
                'dica': palavra.dica,
                'palavra_oculta': palavra_oculta,
                'palavra_id': palavra.id,
                'tentativas_restantes': 6
            }
            return render(request, 'hangmangame.html', context)
        return render(request, 'hangmangame.html', {'error': 'Nenhuma palavra encontrada'}, status=404)

    def post(self, request):
        tentativa = request.POST.get('tentativa', '')
        palavra_id = request.POST.get('palavra_id')
        palavra = Palavra.objects.get(pk=palavra_id)

        palavra_oculta = request.POST.get('palavra_oculta', '')
        tentativas_restantes = int(request.POST.get('tentativas_restantes', 6))

        if tentativa in palavra.palavra:
            palavra_oculta = list(palavra_oculta)
            for i, char in enumerate(palavra.palavra):
                if char == tentativa:
                    palavra_oculta[i] = tentativa
            palavra_oculta = ''.join(palavra_oculta)
        else:
            tentativas_restantes -= 1

        context = {
            'dica': palavra.dica,
            'palavra_oculta': palavra_oculta,
            'tentativas_restantes': tentativas_restantes,
            'palavra_id': palavra.id
        }

        if palavra.palavra == palavra_oculta:
            context['message'] = 'Você ganhou!'
        elif tentativas_restantes <= 0:
            context['message'] = 'Você perdeu! A palavra era: ' + palavra.palavra

        return render(request, 'hangmangame.html', context)