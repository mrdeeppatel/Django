from django.db import models

# Create your models here.
class Product(models.Model):
    pname= models.CharField(max_length=20)
    pprice= models.IntegerField()
    
    def __str__(self):
        return self.pname
    
class GeeksModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name