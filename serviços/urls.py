from unicodedata import name    
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('excluir/<int:id>', views.excluir, name='excluir')
]