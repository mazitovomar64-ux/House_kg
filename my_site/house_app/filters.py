from django_filters.rest_framework import FilterSet
from .models import Property



class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'region' : ['exact'],
            'city': ['exact'],
            'district': ['exact'],
            'property_type': ['exact'],
            'address':['exact'],
            'condition': ['exact'],
            'rooms': ['exact'],
            'total_floor':['exact'],
            'floor':['exact'],
            'price': ['gt','lt'],
        }
