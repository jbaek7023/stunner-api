from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    # Chinese, Mexicans..... so on
    cuisine = models.CharField(null=True, blank=True, max_length=50)
    longitude = models.CharField(null=True, blank=True, max_length=50)
    latitude = models.CharField(null=True, blank=True, max_length=50)
    rate = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    menus = models.ManyToManyField(Menu)
    link = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name
