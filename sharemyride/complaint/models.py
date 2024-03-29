from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=500)
    status = models.CharField(max_length=100)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'complaint'

