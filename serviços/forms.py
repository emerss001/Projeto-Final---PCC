from django.forms import ModelForm
from .models import serviço


class serviçoForm(ModelForm):
    class Meta:
        model = serviço
        fields = "__all__"