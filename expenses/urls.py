from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ExpenseViewSet, MonthlyReportView
from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [

    # Frontend routes
    path('', views.index, name="index"),
    path('categories/', views.categories, name="categories"),
    path('expenses/', views.expenses, name="expenses"),
    path('reports/', views.reports, name="reports"),
]

