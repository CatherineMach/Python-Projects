from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home Page when requested.
def home(request):
    form = TransactionForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        content = {'form': form}
    # Adds content of form to page
    return render(request, 'checkbook/index.html')


# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves new account
            return redirect('index')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html')


# This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html')


# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']# Check to see if the submitted form is valid and if so, saves the form
            form.save()    # Saves the transaction form
            return balance(request, pk)   # Redirects the user to the home page after form submission
    # Pass content to the template in a dictionary
    content = {'form': form}
    # Adds content of form to page
    return render(request, 'checkbook/AddTransaction.html')
