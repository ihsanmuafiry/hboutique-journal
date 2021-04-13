import  django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CashFlowFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date",lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    desc = CharFilter(field_name='desc',lookup_expr='icontains')
    class Meta:
        model = cashFlow
        fields = '__all__'
        exclude = ['date', 'saldoCredit', 'saldoDebit']

