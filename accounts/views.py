from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import User_reg
class RegisterUser(CreateView):
    form_class = User_reg
    template_name = 'adduser.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    ...

