from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ExpenseListCreatView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self, serilizer):
        serilizer.save(user=self.request.user)
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by("-create_at")


class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)






