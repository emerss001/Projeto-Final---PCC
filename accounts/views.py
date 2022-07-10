from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import make_password
from django.views import generic
from usuario.forms import UsuarioForm


from django.urls import reverse_lazy

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, name = name, password = password)

        if user.is_active:
            login(request, user)
    
       

def logout(request):
    logout(request)

class PasswordChangeDoneView(generic.CreateView):
    template_name = 'perfil/perfil.html'


