from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views
# from .views import TripViewSet, ExpenseViewSet, SettlementViewSet

router = DefaultRouter()
router.register(r"trips", TripViewSet, basename="trip")
router.register(r"expenses", ExpenseViewSet, basename="expense")
router.register(r"settlements", SettlementViewSet, basename="settlement")
urlpatterns = [
    path('',views.home,name='home'),
    path("api/", include(router.urls)),
]