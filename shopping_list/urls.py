from django.urls import path

from . import views


urlpatterns = [
    path('listy_zakupow/', views.ShoppingListView.as_view(), name='shopping_lists'),
    path('lista/<int:pk>/', views.ShoppingDetailView.as_view(), name='shopping_list_detail'),
]