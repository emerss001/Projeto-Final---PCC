from django import forms
from django.forms import ModelForm
from .models import Cliente


class CriarCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'pagamento', 'tel', 'Serviço')
        labels = {'nome':'Nome', 'pagamento':'Último pagamento', 'tel':'Telefone'}

class EditarCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'pagamento', 'tel')
        labels = {'nome':'Nome', 'pagamento':'Último pagamento', 'tel':'Telefone'}