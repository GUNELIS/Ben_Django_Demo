from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    # check for login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        # Authetication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Yoare logged in')
            return redirect('home')
        else:
            messages.success(request,'There was an error logging in try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out ...')
    return redirect('home')

def select_account_manager(request):
    account_managers = AccountManager.objects.all()
    if request.method == 'POST':
        selected_account_manager_uname = request.POST['account_manager_username']
        request.session['selected_account_manager_username'] = selected_account_manager_uname
        return redirect('shop_for_services')
    return render(request, 'select_account_manager.html', {'account_managers': account_managers})

def shop_for_services(request):
    selected_account_manager_username = request.session.get('selected_account_manager_username')
    account_manager = AccountManager.objects.get(user__username=selected_account_manager_username)
    service_providers = account_manager.service_providers.all()
    services = Service.objects.filter(service_provider__in=service_providers)
    return render(request, 'shop_for_services.html', {'services': services})


@login_required
def past_orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'past_orders.html', {'orders': orders})



@login_required
def order_complete(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        service_ids = request.POST['service_ids'].split(',')
        services = Service.objects.filter(id__in=service_ids)
        
        selected_account_manager_id = request.session.get('selected_account_manager_id')
        account_manager = AccountManager.objects.get(id=selected_account_manager_id)

        order = Order.objects.create(
            customer=customer,
            account_manager=account_manager,
        )
        order.services.set(services)
        order.save()

        messages.success(request, 'The order was completed')
        return redirect('home')
    else:
        return render(request, 'home.html')

    # Get all orders associated with this account manager
    # Get all service providers associated with this account manager
    # Get all customers associated with this account manager
    # Get all services associated with this account manager's service providers

@login_required
def account_manager_page(request):
    try:
        account_manager = AccountManager.objects.get(user=request.user)
    except AccountManager.DoesNotExist:
        return render(request, 'not_account_manager.html')

    orders = Order.objects.filter(account_manager=account_manager)
    service_providers = account_manager.service_providers.all()
    customers = account_manager.customers.all()
    services = Service.objects.filter(service_provider__in=service_providers)
    return render(request, 'account_manager_page.html', {'orders': orders, 'service_providers': service_providers, 'customers': customers, 'services': services})
