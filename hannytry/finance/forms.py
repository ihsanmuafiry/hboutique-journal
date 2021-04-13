from django.forms import ModelForm
from .models import cashFlow

class cashflowForm(ModelForm):
    class Meta:
        model = cashFlow
        fields = ['tipe','desc','date','price']

