from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .models import Income
from .serializers import IncomeSerializer
from .views import IncomeViewSet


router = DefaultRouter()


router.register('income', IncomeViewSet)

urlpatterns = [
    path('',include(router.urls))
]