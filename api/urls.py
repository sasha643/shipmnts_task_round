from django.urls import path
from django.contrib import admin
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('locations', LocationCreateView.as_view(), name='add-location'),
    path('roads', RoadCreateView.as_view(), name='add-road'),
    path('traffic-updates', TrafficUpdateCreateView.as_view(), name='update-traffic'),
    path('shortest-path', ShortestPathView.as_view(), name='shortest-path'),
]
