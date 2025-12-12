from django.urls import path
from . import views

urlpatterns = [
    path("",views.ExpenseListCreatView.as_view(),name="expense-list-create"),
    path("<int:pk>/",views.ExpenseRetrieveUpdateDestroyView.as_view(),name="expense-detail"),
]