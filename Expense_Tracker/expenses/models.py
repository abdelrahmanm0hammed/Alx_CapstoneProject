from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(null=False, blank=False)
    create_at =models.DateTimeField(auto_now_add=True)