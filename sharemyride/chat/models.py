from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat = models.CharField(max_length=50)
    from_id = models.IntegerField()
    to_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chat'
