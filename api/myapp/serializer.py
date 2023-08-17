from rest_framework import serializers
from api.myapp.models import OverpassData
from api.myapp.models import OverpassPoliceData
from api.myapp.models import OverpassFireData

class OverpassDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverpassData
        fields = ['osm_id','lon','lat','name','emergency_facility']

class OverpassPoliceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverpassPoliceData
        fields = ['osm_id','lon','lat','name','amenity']
class OverpassFireDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverpassFireData
        fields = ['osm_id','lon','lat','name','amenity']