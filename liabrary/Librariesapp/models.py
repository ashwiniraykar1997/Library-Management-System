from django.db import models

# Create your models here.
class books(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    Author = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    #class Meta:
    #    db_table:"librariesapp_books"

class auth_user(models.Model):
    
    class Meta:
        db_table:"auth_user"