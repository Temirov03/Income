from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Income
from .serializers import IncomeSerializer
from django.urls import path,include

# Create your views here.

class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
