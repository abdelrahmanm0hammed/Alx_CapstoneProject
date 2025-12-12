from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]