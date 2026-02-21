from django.shortcuts import render
from .models import Income
from .serializers import IncomeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IncomeListCreateView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
    def get_queryset(self):
        return Income.objects.filter(user=self.request.user).order_by("-create_at")

class IncomeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)
