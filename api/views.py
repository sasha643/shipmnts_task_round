from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .functions import *

class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RoadCreateView(generics.CreateAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

    def post(self, request, *args, **kwargs):
        traffic_condition = request.data.get('traffic_condition')
        if traffic_condition not in dict(Road.TRAFFIC_CONDITIONS):
            return Response({"error": "Invalid traffic condition."}, status=status.HTTP_400_BAD_REQUEST)
        
        response = super().post(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

class TrafficUpdateCreateView(generics.CreateAPIView):
    queryset = TrafficUpdate.objects.all()
    serializer_class = TrafficUpdateSerializer

class ShortestPathView(APIView):
    def get(self, request, *args, **kwargs):
        start_location_id = request.query_params.get('start_location_id')
        end_location_id = request.query_params.get('end_location_id')
        
        if not start_location_id or not end_location_id:
            return Response({"error": "Both start_location_id and end_location_id are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            path, total_distance, estimated_time = calculate_shortest_path(start_location_id, end_location_id)
            return Response({
                'path': path,
                'total_distance': total_distance,
                'estimated_time': estimated_time
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)