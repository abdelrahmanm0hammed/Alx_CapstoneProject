from rest_framework import serializers
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Income
        fields = ["id", "user", "amount", "source", "date", "description", "created_at"]