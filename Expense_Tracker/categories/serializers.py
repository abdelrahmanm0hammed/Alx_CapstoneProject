from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields ="__all__"
       
        