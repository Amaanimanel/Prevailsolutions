from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


from .models import *

class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        exclude = ['user']

class InvestmentForm(ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'

class UserInvestmentForm(ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'
        exclude = ['user', 'investor']



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
