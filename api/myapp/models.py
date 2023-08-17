from django.contrib.gis.db import models


# Create your models here.
class OverpassData(models.Model):
    osm_id = models.CharField(primary_key=True,max_length=30,null=False)
    lon = models.DecimalField(max_digits=20,decimal_places=13)
    lat = models.DecimalField(max_digits=20,decimal_places=13)
    name = models.CharField(max_length = 50,null=True)
    emergency_facility = models.CharField(max_length=10,null=True)
    loc_pnt = models.PointField(null=True,blank=True)

    class Meta:
        db_table = "overpass_turbo"

class OverpassPoliceData(models.Model):
    osm_id = models.CharField(primary_key=True,max_length=30,null=False)
    lon = models.DecimalField(max_digits=20,decimal_places=13)
    lat = models.DecimalField(max_digits=20,decimal_places=13)
    name = models.CharField(max_length = 100,null=True)
    amenity = models.CharField(max_length=30,null=True)
    loc_pnt = models.PointField(null=True,blank=True)
    class Meta:
        db_table = "overpass_police"

class OverpassFireData(models.Model):
    osm_id = models.CharField(primary_key=True,max_length=30,null=False)
    lon = models.DecimalField(max_digits=20,decimal_places=13)
    lat = models.DecimalField(max_digits=20,decimal_places=13)
    name = models.CharField(max_length = 100,null=True)
    amenity = models.CharField(max_length=30,null=True)
    loc_pnt = models.PointField(null=True,blank=True)
    class Meta:
        db_table = "overpass_fire"


