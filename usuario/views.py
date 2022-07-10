from django.shortcuts import render, redirect
from .forms import UsuarioForm, EditUser, EditSenha
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic


# Create your views here.

def criar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/accounts/login')
    else:
        form = UsuarioForm()
    
    context = {
        'form': form
    }

    return render(request, 'usuario/criar.html', context)


@login_required()
def editar(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = EditUser(request.POST, instance = usuario)

    if request.method == 'POST':
        form = EditUser(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')

    else:
        print('WWWWWWWWWWWW')

    context = {
        'form': form,
        'usuario': usuario
    }
    
    return render(request, 'usuario/listar.html', context)



class PasswordChangeView(generic.CreateView):
    form_class = PasswordChangeForm
    template_name = 'editar.html'




