from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import serviçoForm
from .models import serviço
# Create your views here.

@login_required()
def listar(request):
    serviços = serviço.objects.all()
     
    if request.method == "POST":
        form = serviçoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/serviços/")
    else:
        form = serviçoForm()
    
    context = {
        'form': form,
        'serviços': serviços
    }
    return render(request,'serviços/servicos.html', context)


@login_required()
def editar(request, id):
    s = serviço.objects.get(pk=id)
    form = serviçoForm(request.POST, instance=s)
    if request.method == "POST":
        form = serviçoForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect("/serviços/")
    
    context = {
        'form': form,
        'serviço': s
    }
    return render(request,'serviços/editar.html', context)


@login_required()
def excluir(request, id):
    s = get_object_or_404(serviço, pk=id)
    s.delete()
    return redirect('/serviços/')
