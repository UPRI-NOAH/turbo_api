import django_filters
from api.myapp.models import OverpassData, OverpassPoliceData, OverpassFireData
class OverpassDataFilter(django_filters.FilterSet):
    class Meta:
        model = OverpassData
        fields = {
            'osm_id':['exact'],
            'emergency_facility':['exact'],
            'name':['exact']
        }
class OverpassPoliceDataFilter(django_filters.FilterSet):
    class Meta:
        model = OverpassPoliceData
        fields = {
            'osm_id':['exact'],
            'name': ['exact'],
            'amenity':['exact'],
        }
class OverpassFireDataFilter(django_filters.FilterSet):
    class Meta:
        model = OverpassFireData
        fields = {
            'osm_id':['exact'],
            'name': ['exact'],
            'amenity':['exact'],
        }