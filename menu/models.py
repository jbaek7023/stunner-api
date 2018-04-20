from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    # Chinese, Mexicans..... so on
    menu_type = models.CharField(null=True, blank=True, max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(null=True, blank=True, max_length=50)
    review_count = models.IntegerField(default=0)
    current_rate = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name
