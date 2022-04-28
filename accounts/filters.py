from pyexpat import model
import django_filters
from django_filters import DateFilter

from .models import *

class InvestmentFilter (django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta: 
        model = Investment
        fields = '__all__'
        exclude = ['investor', 'date_created', 'user', 'address', 'email', 'phone', 'amount',]