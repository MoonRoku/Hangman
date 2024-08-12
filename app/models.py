from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nickname")
    senha = models.CharField(max_length=100, verbose_name="Password")
    def __str__(self):
            return f"'Usuário:' {self.nome}"
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        
class ClasseDePalavra(models.Model):
    NDC = models.CharField(max_length=100, verbose_name='Classe de palavra')
    def __str__(self):
            return f"'Nome da classe:' {self.NDC}"
    class Meta:
        verbose_name = "Classe de palavra"
        verbose_name_plural = "Classe de palavras"

class Palavra(models.Model):
    palavra = models.CharField(max_length=20, verbose_name='Palavra')
    dica = models.CharField(max_length=100, verbose_name="Dica da palavra")
    CDP = models.ForeignKey(ClasseDePalavra, on_delete=models.CASCADE, verbose_name="Classe da palavra")
    def __str__(self):
            return f"{self.palavra}',' {self.CDP}"
    class Meta:
        verbose_name = "Palavra"
        verbose_name_plural = "palavras"
        
class Jogo(models.Model):
    tempo = models.TimeField(verbose_name='Tempo de conclusão')
    jogador = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Jogador")
    def __str__(self):
            return f"O jogador: {self.jogador}' concluiu em' {self.tempo} tempo."
    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"