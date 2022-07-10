from django.shortcuts import render

def modelos(request):
    return render(request, 'modelos/modelos.html')