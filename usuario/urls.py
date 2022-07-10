from unicodedata import name    
from django.urls import URLPattern, path, include
from . import views
from django.contrib.auth import views as auth_views
namespace = 'usuario'

urlpatterns = [
    path('criar', views.criar, name='criar'),
    path('editar/<int:id>', views.editar, name='editar'),
   # path('editarSenha/<int:id>', views.editarSenha, name='editarSenha'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
]