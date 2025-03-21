from rest_framework import serializers
from .models import Trip, Expense, Settlement
from django.contrib.auth.models import User

class TripSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source="created_by.username")  # Show username in GET
    members = serializers.SerializerMethodField()  # Convert members list to usernames

    class Meta:
        model = Trip
        fields = ["id", "name", "created_by_name", "members"]

    def get_members(self, obj):
        """ Convert member IDs to usernames """
        return [user.username for user in obj.members.all()]

    def create(self, validated_data):
        """ Convert usernames to User objects before saving """
        request = self.context.get("request")
        
        if request and request.data.get("created_by_name"):
            user = User.objects.get(username=request.data["created_by_name"])
            validated_data["created_by"] = user
        
        # Convert member usernames to User objects
        member_usernames = request.data.get("members", [])  # Get member names from request
        members = User.objects.filter(username__in=member_usernames)  # Fetch User objects
        validated_data.pop("members", None)  # Remove members from validated_data, handled separately

        trip = super().create(validated_data)  # Create Trip instance
        trip.members.set(members)  # Assign members to the trip
        return trip
class ExpenseSerializer(serializers.ModelSerializer):
    trip_name = serializers.CharField(source="trip.name", read_only=True)  # Display trip name in GET
    paid_by_name = serializers.CharField(source="paid_by.username", read_only=True)  # Display username in GET

    class Meta:
        model = Expense
        fields = ["id", "trip_name", "paid_by_name", "amount", "description", "created_at"]

    def create(self, validated_data):
        """ Convert trip name and paid_by username to objects before saving """
        request = self.context.get("request")

        # Get trip instance by name
        if request and request.data.get("trip_name"):
            trip = Trip.objects.get(name=request.data["trip_name"])
            validated_data["trip"] = trip

        # Get user instance by username
        if request and request.data.get("paid_by_name"):
            user = User.objects.get(username=request.data["paid_by_name"])
            validated_data["paid_by"] = user

        return super().create(validated_data)

class SettlementSerializer(serializers.ModelSerializer):
    trip_name = serializers.CharField(source="trip.name", read_only=True)  # Show trip name in GET
    payer_name = serializers.CharField(source="payer.username", read_only=True)  # Show payer name in GET
    payee_name = serializers.CharField(source="payee.username", read_only=True)  # Show payee name in GET

    class Meta:
        model = Settlement
        fields = ["id", "trip_name", "payer_name", "payee_name", "amount", "status"]

    def create(self, validated_data):
        """ Convert trip name, payer name, and payee name to objects before saving """
        request = self.context.get("request")

        # Get trip instance by name
        if request and request.data.get("trip_name"):
            trip = Trip.objects.get(name=request.data["trip_name"])
            validated_data["trip"] = trip

        # Get payer instance by username
        if request and request.data.get("payer_name"):
            payer = User.objects.get(username=request.data["payer_name"])
            validated_data["payer"] = payer

        # Get payee instance by username
        if request and request.data.get("payee_name"):
            payee = User.objects.get(username=request.data["payee_name"])
            validated_data["payee"] = payee

        return super().create(validated_data)