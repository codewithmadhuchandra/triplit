from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="trips")

class Expense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Settlement(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, related_name="payer", on_delete=models.CASCADE)
    payee = models.ForeignKey(User, related_name="payee", on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.BooleanField(default=False)