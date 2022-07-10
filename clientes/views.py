from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import CriarCliente, EditarCliente
from .models import Cliente
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from serviços.models import serviço
from django.urls import reverse

@login_required
def listar(request):
    cts = Cliente.objects.all()
    context = {
        'cts': cts, 
    }

    return render(request, 'clientes/listar.html', context)

@login_required
def clientes(request, id):
    servico = serviço.objects.get(pk=id)
    cts = Cliente.objects.filter(Serviço=servico)

    if request.method == 'POST':
        form = CriarCliente(request.POST)
        form.instance.user = request.user
        
        if form.is_valid():
            form.save()
            return redirect(reverse('clientes', args=[id]))
            

    else:
            form = CriarCliente

    context = {
        'form': form,
        'cts': cts, 
        'servico' : servico
        }


    return render(request, 'clientes/clientes.html', context)
   


@login_required()
def editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    s = cliente.Serviço.id
    form = EditarCliente(instance=cliente)

    if request.method == 'POST':
        form = EditarCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(reverse('clientes', args=[s]))
    
    context = {'form': form, 'cliente': cliente}

    return render(request, 'clientes/mult.html', context)

def excluir(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    s = cliente.Serviço.id
    cliente.delete()
    return redirect(reverse('clientes', args=[s]))

