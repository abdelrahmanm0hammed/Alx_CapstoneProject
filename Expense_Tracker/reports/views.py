from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from incomes.models import Income
import csv
from django.http import HttpResponse
from django.db.models.functions import ExtractMonth


class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")

        if year is None or month is None:
            return Response({"error":"Please provide year and month"}, status=400)
        year = int(year)
        month = int(month)

        total_expense = (
            Expense.objects.filter(user=request.user, date__year=year, date__month=month)
            .aggregate(total=Sum("amount"))
            .get("total") or 0
        )
        total_income = (
            Income.objects.filter(user=request.user, date__year=year, date__month=month)
            .aggregate(total=Sum("amount"))
            .get("total") or 0
        )
       
        return Response({
            "total_income":total_income,
            "total_expense":total_expense,
            "net_balance": total_income - total_expense
            
        })
    
class MonthlyReportCSVExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")
        
        if not year or not month:
            return HttpResponse("Year and month required", status=400)
        try:
            year = int(year)
            month = int(month)
        except ValueError:
            return HttpResponse("Year and month must be integers", status=400)
        
        #filter data
        expenses = Expense.objects.filter(user=request.user, date__year=year, date__month=month)
        incomes = Income.objects.filter(user=request.user, date__year=year, date__month=month)

        #create http response with csv content type
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f'attachment; filename="report_{year}_{month}.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(["Type", "Category/Source", "Amount", "Date", "Description"])

        #write incomes
        for income in incomes:
            writer.writerow([
                "Income",
                getattr(income, "source", ""),
                income.amount,
                income.date,
                income.description
            ])

        #write expenses
        for expense in expenses:
            writer.writerow([
                "Expense",
                getattr(expense,"category", ""),
                expense.amount,
                expense.date,
                expense.description
            ])
        return response

class YearlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = request.query_params.get("year")

        if not year:
            return Response({"error": "Year is required"}, status=400)
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Year must be integer "}, status=400)
        
        # Group Expenses by month
        expense_data = (
            Expense.objects.filter(user=request.user, date__year=year)
            .annotate(month=ExtractMonth("date"))
            .values("month")
            .annotate(total_expense=Sum("amount"))
            .order_by("month")
        )
        # Group Income by month 
        income_data = (
            Income.objects.filter(user=request.user, date__year=year)
            .annotate(month=ExtractMonth("date"))
            .values("month")
            .annotate(total_income=Sum("amount"))
            .order_by("month")
        )
        # convert querysets into dictionaries for easier merging
        expense_dict = {item["month"]: item["total_expense"] for item in expense_data}
        income_dict = {item["month"]: item["total_income"] for item in income_data}

        # Get all months that appear in either income or expense
        all_month = sorted(set(expense_dict.keys()) | set(income_dict.keys()))

        monthly_data = []

        for month in all_month:
            total_income = income_dict.get(month, 0)
            total_expense = expense_dict.get(month, 0)

            monthly_data.append({
                "month":month,
                "total_income": total_income,
                "total_expense": total_expense,
                "net_balance": total_income - total_expense
            })
        return Response({
            "year": year,
            "monthly_data":monthly_data
        })