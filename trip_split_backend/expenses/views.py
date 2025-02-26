from django.shortcuts import render

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

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class SettlementViewSet(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer