from rest_framework import serializers
from .models import Location, Road, TrafficUpdate

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'

class TrafficUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficUpdate
        fields = '__all__'