from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ExpenseListCreatView(generics.ListCreateAPIView):
    queryset= Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    


class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]






