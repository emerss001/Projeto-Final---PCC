from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    telefone = models.CharField(max_length=16, null=True)
    cpf = models.CharField(max_length=14, null=True)
    cidade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username