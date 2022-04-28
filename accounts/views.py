from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from .models import *
from .forms import InvestmentForm, CreateUserForm,InvestorForm,UserInvestmentForm
from .filters import InvestmentFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	investments = Investment.objects.all()
	investors = Investor.objects.all()

	total_investors = investors.count()

	total_investments = investments.count()
	matured = investments.filter(typeofpos='Matured').count()
	verified = investments.filter(typeofpos='Verified').count()
	pending = investments.filter(typeofpos='Pending').count()


	context = {'investments':investments, 'investors':investors,
	'total_investments':total_investments, 'total_investors':total_investors,'verified':verified,
	'pending':pending, 'matured':matured }

	return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['investor'])
def userPage(request):
    investments = request.user.investor.investment_set.all()
    
    total_investments = investments.count()
    matured = investments.filter(typeofpos='Matured').count()
    verified= investments.filter(typeofpos='Verified').count()
    pending = investments.filter(typeofpos='Pending').count()
	    
    context = {'investments':investments,'total_investments':total_investments,'verified':verified,
	'pending':pending, 'matured':matured}

    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'investor'])
def accountSettings(request):
    investor = request.user.investor
    form = InvestorForm(instance=investor)

    if request.method == 'POST':
        form = InvestorForm(request.POST, request.FILES, instance=investor)
        if form.is_valid():
            form.save()

    context ={'form':form}
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'investor'])
def projects(request):


	return render(request, 'accounts/projects.html', {'projects':projects})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'investor'])
def faqs(request):
	
	return render(request, 'accounts/faqs.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def investor(request, pk_test):
	investor = Investor.objects.get(id=pk_test)

	investments = investor.investment_set.all()
	investment_count = investments.count()

	myFilter = InvestmentFilter(request.GET, queryset=investments)
	investments = myFilter.qs 

	context = {'investor':investor, 'investments':investments, 'investment_count':investment_count,
	'myFilter':myFilter}
	return render(request, 'accounts/investor.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def makeInvestment(request, pk):
	InvestmentFormSet = inlineformset_factory(Investor, Investment, fields=('project','amount',), extra=1 )
	investor = Investor.objects.get(id=pk)
	formset = InvestmentFormSet(queryset=Investment.objects.none(),instance=investor)
	#form = OrderForm(initial={'investor':investor})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = InvestmentForm(request.POST)
		formset = InvestmentFormSet(request.POST, request.FILES, instance=investor)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'formset':formset}
	return render(request, 'accounts/investment_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['investor'])
def userInvestment(request):
	
    if request.method == 'GET':
        return render(request, 'accounts/user_invest_form.html', {'form':UserInvestmentForm()})
    else:
        try:
            form = UserInvestmentForm(request.POST or None)
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
			
            return redirect('user-page')
			
        except ValueError:
            return render(request, 'accounts/user_invest_form.html', {'form':UserInvestmentForm(), 'error':'Bad data passed in. Try again.'})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'investor'])
def updateInvestment(request, pk):

	investment = Investment.objects.get(id=pk)
	form = InvestmentForm(instance=investment)

	if request.method == 'POST':
		form = InvestmentForm(request.POST, request.FILES, instance=investment)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/investment_update_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'investor'])
def deleteInvestment(request, pk):
	investment = Investment.objects.get(id=pk)
	if request.method == 'POST':
		investment.delete()
		return redirect('/')

	context = {'investment':investment}
	return render(request, 'accounts/delete.html', context)