from django.contrib import admin
from .models import OverpassData
from .models import OverpassPoliceData
from .models import OverpassFireData

# Register your models here.
admin.site.register(OverpassData)
admin.site.register(OverpassPoliceData)
admin.site.register(OverpassFireData)
