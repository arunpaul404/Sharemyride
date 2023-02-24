from django.db import models

# Create your models here.
class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    route = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
