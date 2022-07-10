from django.db import models


ESTADO_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AM", "Amazonas"),
    ("AP", "Amapá"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MG", "Minas Gerais"),
    ("MS", "Mato Grosso do Sul"),
    ("MT", "Mato Grosso"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("PR", "Paraná"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("RS", "Rio Grande do Sul"),
    ("SC", "Santa Catarina"),
    ("SE", "Sergipe"),
    ("SP", "São Paulo"),
    ("TO", "Tocantins")
)

CIDADE_CHOICES = ()

class ReciboPadrao(models.Model):

    data = models.DateField()
    nrro_recibo = models.CharField(max_length=5)
    nome_pagador = models.CharField(max_length=100)
    cpf_cnpj_pagador = models.CharField(max_length=19)
    nome_beneficiario = models.CharField(max_length=100)
    cpf_cnpj_beneficiario = models.CharField(max_length=19)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=100, choices=CIDADE_CHOICES)
    descricao = models.CharField(max_length=200, blank=True)
    valor = models.CharField(max_length=10)
    celular = models.CharField(max_length=19)

    
        
    

