from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Trip(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="trips")

    def get_member_count(self):
        return self.members.count()

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

@receiver(post_save, sender=Expense)
def create_settlements(sender, instance, **kwargs):
    trip = instance.trip
    members = trip.members.exclude(id=instance.paid_by.id)  # Exclude payer
    num_members = trip.get_member_count()
    
    if num_members > 1:
        share = instance.amount / num_members
    
        for member in members:
            Settlement.objects.create(
                trip=trip,
                payer=member,
                payee=instance.paid_by,
                amount=share,
                status=False
            )