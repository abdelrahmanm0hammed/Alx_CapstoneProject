from django.urls import path
from . import views

urlpatterns = [
    path("monthly/", views.MonthlyReportView.as_view(), name="monthly-report"),
]