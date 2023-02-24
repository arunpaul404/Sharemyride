from django.db import models

# Create your models here.
class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    registered_no = models.IntegerField()
    type = models.CharField(max_length=25)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehicles'