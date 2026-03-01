from django.urls import path
from . import views

urlpatterns = [
    path("monthly/", views.MonthlyReportView.as_view(), name="monthly-report"),
    path("monthly/export/",views.MonthlyReportCSVExportView.as_view(), name="monthly-report-export"),
    path("yearly/",views.YearlyReportView.as_view(), name='yearly-report'),
    path("dashboard/",views.DashboardSummaryView.as_view(),name="dashboard-summary")
]