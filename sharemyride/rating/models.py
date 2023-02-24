from django.db import models

# Create your models here.
class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rating'
