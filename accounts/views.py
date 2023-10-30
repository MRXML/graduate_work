from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    ...