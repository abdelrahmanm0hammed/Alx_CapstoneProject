from django.shortcuts import render
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense
from incomes.models import Income


class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.query_params)
        year = request.query_params.get("year")
        month = request.query_params.get("month")

        if  year is None or month is None:
            return Response(
                {"error":"Please provide year and month"},status=400
            )

        
        year = int(year)
        month = int(month)
        
        

        total_expense = (Expense.objects.filter(
            user=request.user,
            date__year =year,
            date__month = month
        ).aaggregate(total=Sum("amount")).get("total") or 0)

        total_income = (Income.objects.filter(
            user =request.user,
            date__year =year,
            date__month = month,).aaggregate(total=Sum("amount")).get("total") or 0)
        
        
        net_balance = total_income - total_expense

        return Response({
            "month":f"{year}-{month}",
            "total_income":total_income,
            "total_expense":total_expense,
            "net_balance":net_balance,

        })
        
