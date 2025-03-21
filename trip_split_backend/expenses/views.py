from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .models import Trip, Expense, Settlement
from .serializers import TripSerializer, ExpenseSerializer, SettlementSerializer

# Create your views here.
from rest_framework import viewsets
from .models import Trip, Expense, Settlement
from .serializers import TripSerializer, ExpenseSerializer, SettlementSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Triplit</h1>')

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=["get"])
    def member_count(self, request, pk=None):
        trip = self.get_object()
        return Response({"member_count": trip.members.count()})

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=True, methods=["get"])
    def trip_expenses(self, request, pk=None):
        expenses = Expense.objects.filter(trip_id=pk)
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)

class SettlementViewSet(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
    @action(detail=True, methods=["get"])
    def trip_settlements(self, request, pk=None):
        settlements = Settlement.objects.filter(trip_id=pk)
        serializer = self.get_serializer(settlements, many=True)
        return Response(serializer.data)
