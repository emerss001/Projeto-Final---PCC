from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.http import HttpResponse



@login_required
def perfil(request):
    return render(request, 'perfil/perfil.html')
