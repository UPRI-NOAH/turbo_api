# Generated by Django 4.2.4 on 2023-08-15 14:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverpassData',
            fields=[
                ('osm_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('lon', models.DecimalField(decimal_places=13, max_digits=20)),
                ('lat', models.DecimalField(decimal_places=13, max_digits=20)),
                ('name', models.CharField(max_length=50, null=True)),
                ('emergency_facility', models.CharField(max_length=10, null=True)),
                ('loc_pnt', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'overpass_turbo',
            },
        ),
    ]
