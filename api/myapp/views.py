from django.shortcuts import render
from rest_framework.views import APIView
import requests
from api.myapp.models import OverpassData
from api.myapp.models import OverpassPoliceData
from api.myapp.models import OverpassFireData
from api.myapp.serializer import OverpassDataSerializer
from api.myapp.serializer import OverpassPoliceDataSerializer
from api.myapp.serializer import OverpassFireDataSerializer
from rest_framework.response import Response
from api.myapp.data import ExtractData
from api.myapp.police import ExtractPoliceData
from api.myapp.fire import ExtractFireData
from api.myapp.filters import OverpassDataFilter
from api.myapp.filters import OverpassPoliceDataFilter
from api.myapp.filters import OverpassFireDataFilter
from django.core.serializers import serialize
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework import viewsets
import json


class OverpassDataViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = OverpassData.objects.all()
    serializer_class = OverpassDataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OverpassDataFilter

    def list(self,request):
        ExtractData()
        queryset = self.get_queryset()
        queryset = self.filterset_class(self.request.GET,queryset=queryset)
       
        data = serialize("geojson",queryset.qs)
        return Response(data = json.loads(data))

class OverpassPoliceDataViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = OverpassPoliceData.objects.all()
    serializer_class = OverpassPoliceDataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OverpassPoliceDataFilter

    def list(self,request):
        ExtractPoliceData()
        queryset = self.get_queryset()
        queryset = self.filterset_class(self.request.GET,queryset=queryset)
       
        data = serialize("geojson",queryset.qs)
        return Response(data = json.loads(data))
class OverpassFireDataViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = OverpassFireData.objects.all()
    serializer_class = OverpassFireDataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OverpassFireDataFilter

    def list(self,request):
        ExtractFireData()
        queryset = self.get_queryset()
        queryset = self.filterset_class(self.request.GET,queryset=queryset)
       
        data = serialize("geojson",queryset.qs)
        return Response(data = json.loads(data))


       
