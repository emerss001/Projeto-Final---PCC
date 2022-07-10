from django import forms
from .models import ReciboPadrao

class RcbPadrao(forms.ModelForm):
    class Meta:
        model = ReciboPadrao
        fields = "__all__"

