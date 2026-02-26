from django.urls import path
from . import views

urlpatterns = [
    path("monthly/", views.MonthlyReportView.as_view(), name="monthly-report"),
    path("monthly/export/",views.MonthlyReportCSVExportView.as_view(), name="monthly-report-export")
]