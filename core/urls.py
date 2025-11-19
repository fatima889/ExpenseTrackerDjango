from django.urls import path
from core.views import *


urlpatterns = [

    # expense URLS
    path('list-expenses/', list_expenses, name='list_expenses'),

    # delete expense
    path('delete-expense/<int:expense_id>/', delete_expense, name='delete_expense'),

    # add expense
    path('add-expense/', add_expense , name='add_expense'),

    # edit expense
    path('edit-expense/<int:expense_id>/', edit_expense , name='edit_expense'),
]