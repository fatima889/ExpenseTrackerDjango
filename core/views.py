from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from core.models import *
from core.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def list_expenses(request):
    expenses = Expense.objects.filter(user=request.user)
    #hotels = Hotel.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, 'core/list_expenses.html', context)

@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    expense.delete()
    return redirect('list_expenses')

@login_required
def add_expense(request):
    if request.method == 'POST':
        print(request.POST)
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

            form.save_m2m()

            return redirect('list_expenses')
    else:
        form = ExpenseForm()

    context = {'form': form}
    return render(request, 'core/add_expense.html', context)

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm(instance=expense)

    context = {'form': form, 'hotel': expense}
    return render(request, 'core/edit_expense.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_expenses')
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')