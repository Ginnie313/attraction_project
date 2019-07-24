from django.db import models

# Create your models here.

class Attraction(models.Model):
    attraction_name = models.CharField(max_length=200, default = "None") #Added default so that I could migrate successfully
    height_req = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    fastpass = models.CharField(max_length=200)
    park = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.attraction_name
