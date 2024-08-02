from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Road(models.Model):
    TRAFFIC_CONDITIONS = [
        ('clear', 1),
        ('moderate', 5),
        ('heavy', 10),
    ]
    
    start_location = models.ForeignKey(Location, related_name='start_roads', on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, related_name='end_roads', on_delete=models.CASCADE)
    distance = models.FloatField()
    traffic_condition = models.CharField(max_length=10, choices=TRAFFIC_CONDITIONS)

    def __str__(self):
        return f"{self.start_location} to {self.end_location}"

    def get_traffic_weight(self):
        return dict(self.TRAFFIC_CONDITIONS).get(self.traffic_condition, 1)
    

class TrafficUpdate(models.Model):
    road = models.ForeignKey(Road, related_name='updates', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    traffic_condition = models.CharField(max_length=10, choices=Road.TRAFFIC_CONDITIONS)