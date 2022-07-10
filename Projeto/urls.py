from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('modelos/', include('modelos.urls')),
    path('perfil/', include('perfil.urls')),
    path('usuario/', include('usuario.urls')), 
    path('clientes/', include('clientes.urls')),   
    path('serviços/', include('serviços.urls'))
]
