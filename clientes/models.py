from django.db import models
from django.contrib.auth.models import User
from serviços.models import serviço
from django.contrib.auth import get_user_model

class Cliente(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tel = models.CharField(max_length=19)
    pagamento = models.CharField(max_length=19, blank=True)
    Serviço = models.ForeignKey(serviço, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

