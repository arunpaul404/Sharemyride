from django.db import models

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking = models.CharField(max_length=25)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'booking'
