from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import RcbPadrao
from .models import ReciboPadrao
from django.db.models.query_utils import DeferredAttribute
from num2words import num2words

def home(request):
        recibos = ReciboPadrao.objects.all().delete()
        form = RcbPadrao(request.POST, request.FILES)
        context = {
        'form': form
        }
        return render(request, "home/index.html", context=context)
        




def gerador(request): 
        if request.method == "POST":
            data = request.POST.get('data')
            nrro_recibo = request.POST.get('nro')
            nome_pagador = request.POST.get('nome_pagador')
            cpf_cnpj_pagador = request.POST.get('pagadorcpf')
            nome_beneficiario = request.POST.get('nome_beneficiario')
            cpf_cnpj_beneficiario = request.POST.get('benecpf')
            estado = request.POST.get('estado')
            cidade = request.POST.get('cidade')
            descricao = request.POST.get('desc')
            valor = request.POST.get('valor')
            celular = request.POST.get('celular') 


            rebido = ReciboPadrao.objects.create(
                data = data,
                nrro_recibo = nrro_recibo,
                nome_pagador = nome_pagador,
                cpf_cnpj_pagador = cpf_cnpj_pagador,
                nome_beneficiario = nome_beneficiario,
                cpf_cnpj_beneficiario = cpf_cnpj_beneficiario,
                estado = estado,
                cidade = cidade,
                descricao = descricao,
                valor = valor,
                celular = celular

                )
            rebido.save()
            dados = ReciboPadrao.objects.all()
    
            return render(request, "home/recibo.html", {'dados' : dados})
        return render(request, "home/recibo.html")


def baixar(request):
    dados = ReciboPadrao.objects.all()
    return render(request, "home/imprimir.html", {'dados' : dados})
        
        
        




