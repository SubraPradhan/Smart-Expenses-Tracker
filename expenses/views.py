from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class MonthlyReportView(APIView):
    def get(self, request):
        data = (
            Expense.objects
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )
        return Response(data)



from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def categories(request):
    return render(request, "categories.html")

def expenses(request):
    return render(request, "expenses.html")

def reports(request):
    return render(request, "reports.html")
