from django.db import models

# Create your models here.
class clinica(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    url = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % self.nome


class recuperacao(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=15)
    data = models.DateField()
    email = models.EmailField()
    informacoes = models.TextField()
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)

class solicitar(models.Model):
    protocolo = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    data = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=15)
    clinica = models.ForeignKey(clinica, on_delete=models.CASCADE)