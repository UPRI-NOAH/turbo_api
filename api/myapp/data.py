from api.myapp.models import OverpassData
import requests
def ExtractData():
    overpass_query = """[out:json];area["ISO3166-1"="PH"]["admin_level"="2"]->.a;(node["emergency:social_facility:for"="displaced"](area.a););out;"""
    overpass_url = r"http://overpass-api.de/api/interpreter" 
    response = requests.get(overpass_url,params={'data':overpass_query})
    data = response.json()
    for element in data['elements']:
        if element['type']=='node':
            obj,created = OverpassData.objects.update_or_create(osm_id=element['id'],defaults = {
                'lon':element['lon'],
                'lat':element['lat'],
                'name': 'N/A',
                'emergency_facility':element['tags']['emergency:social_facility']
            }
            )
            if 'name' in element['tags']:
                obj.name = element['tags']['name']

            obj.save()
if __name__=='__main__':
    ExtractData()
