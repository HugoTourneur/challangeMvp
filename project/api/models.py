from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class lodging(models.Model):
  lodging_title = models.CharField(max_length=30)
  start_period = models.DateTimeField()
  end_period = models.DateTimeField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)