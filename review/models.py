from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User)
    rate = models.IntegerField(default=0)
    comment = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.comment
