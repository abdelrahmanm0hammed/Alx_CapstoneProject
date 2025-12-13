from rest_framework import serializers
from .models import Expense
from categories.models import Category

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    class Meta:
        model = Expense
        fields = "__all__"
        