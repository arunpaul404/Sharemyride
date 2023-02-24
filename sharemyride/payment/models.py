from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    payment = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'payment'
