from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from incomes.models import Income

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
       