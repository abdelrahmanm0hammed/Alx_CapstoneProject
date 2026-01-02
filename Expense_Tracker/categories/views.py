from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class CategoryListCreateView(generics.ListCreateAPIView):
    
    serializer_class=CategorySerializer

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the category
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class=CategorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)