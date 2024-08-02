from django.contrib import admin
from .models import *

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_location', 'end_location', 'distance', 'traffic_condition')
    search_fields = ('start_location__name', 'end_location__name', 'traffic_condition')
    list_filter = ('traffic_condition',)

@admin.register(TrafficUpdate)
class TrafficUpdateAdmin(admin.ModelAdmin):
    list_display = ('id', 'road', 'timestamp', 'traffic_condition')
    search_fields = ('road__start_location__name', 'road__end_location__name', 'traffic_condition')
    list_filter = ('traffic_condition', 'timestamp')
