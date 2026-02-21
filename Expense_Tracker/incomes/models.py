from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user} - {self.amount}"