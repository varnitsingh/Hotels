from django.db import models


# Create your models here.
class Resturant(models.Model):
    resturant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    rest_type = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    review = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

class Hours(models.Model):
    resturant_id = models.ForeignKey(Resturant,on_delete=models.CASCADE)
    day = models.CharField(max_length=30)
    opens_at = models.CharField(max_length=30)
    closes_at = models.CharField(max_length=30)
    