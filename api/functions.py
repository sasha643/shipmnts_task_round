from django.db.models import Q
from .models import Location, Road
from heapq import heappop, heappush

def calculate_shortest_path(start_location_id, end_location_id):
    def get_traffic_weight(condition):
        weights = {
            'clear': 1,
            'moderate': 5,
            'heavy': 10
        }
        return weights.get(condition, 1)  # Default to 1 if condition is unknown

    def get_neighbors(location):
        roads = Road.objects.filter(Q(start_location=location) | Q(end_location=location))
        neighbors = []
        for road in roads:
            if road.start_location.id == location.id:
                neighbors.append((road.end_location, road.distance, get_traffic_weight(road.traffic_condition)))
            else:
                neighbors.append((road.start_location, road.distance, get_traffic_weight(road.traffic_condition)))
        return neighbors
    
    start_location = Location.objects.get(id=start_location_id)
    end_location = Location.objects.get(id=end_location_id)
    
    pq = [(0, start_location.id, [])]
    visited = set()
    
    while pq:
        (current_distance, current_location_id, path) = heappop(pq)
        if current_location_id in visited:
            continue
        
        path = path + [current_location_id]
        
        if current_location_id == end_location_id:
            estimated_time = current_distance / 40 
            return path, current_distance, estimated_time
        
        visited.add(current_location_id)
        
        for neighbor, distance, traffic_weight in get_neighbors(Location.objects.get(id=current_location_id)):
            if neighbor.id not in visited:
                heappush(pq, (current_distance + distance * traffic_weight, neighbor.id, path))
    
    return [], 0, 0
