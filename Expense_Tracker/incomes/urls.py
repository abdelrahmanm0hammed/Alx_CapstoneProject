from django.urls import path
from . import views

urlpatterns = [
    path("",views.IncomeListCreateView.as_view(),name="income-list-create"),
    path("<int:pk>/",views.IncomeRetrieveUpdateDestroyView.as_view(),name="income-detail")
]