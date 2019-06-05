from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 48)

    def __str__(self):
        return "{}_token".format(self.user)

class Advertisment(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length = 200)
    cost = models.IntegerField()
    description = models.TextField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    expiration = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.name, self.cost)

class Supplier(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
