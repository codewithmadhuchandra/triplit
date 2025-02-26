from rest_framework import serializers
from .models import Trip, Expense, Settlement

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = "__all__"