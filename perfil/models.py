from django.db import models
from django.contrib.auth.models import User

class perfilUser(models.Model):
        telefone = models.CharField(max_length=16, null=True)
        cpf = models.CharField(max_length=14, null=True)
        cidade = models.CharField(max_length=50, null=True)
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
