from api.myapp.models import OverpassPoliceData
import requests
# import os
# import sys
# import django
# from pathlib import Path


# """
# Update sys path to be able to import project
# packages outside the current folder
# """

# PROJECT_ROOT = Path(_file_).resolve().parents[2]
# sys.path.append(str(PROJECT_ROOT))

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")  # noqa: E402
# django.setup()
def ExtractPoliceData():
    overpass_query = """[out:json];area["ISO3166-1"="PH"]["admin_level"="2"]->.a;(node["amenity"="police"](area.a););out;"""
    overpass_url = r"http://overpass-api.de/api/interpreter" 
    response = requests.get(overpass_url,params={'data':overpass_query})
    data = response.json()
    for element in data['elements']:
        if element['type']=='node':
            obj,created = OverpassPoliceData.objects.update_or_create(osm_id=element['id'],defaults = {
                'lon':element['lon'],
                'lat':element['lat'],
                'name':"N/A",
                'amenity':element['tags']['amenity']
            }
            )
            if 'name' in element['tags']:
                obj.name = element['tags']['name']

            obj.save()
if __name__=='__main__':
    ExtractPoliceData()
