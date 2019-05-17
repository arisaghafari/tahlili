from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    cost = models.IntegerField()
    description = models.TextField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    expiration = models.DateField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
