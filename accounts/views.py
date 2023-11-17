from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('main_page')

from .forms import User_reg
class RegisterUser(CreateView):
    form_class = User_reg
    template_name = 'adduser.html'
    success_url = reverse_lazy('login')



from .forms import User_log
class Login(LoginView):
    form_class = User_log
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('main_page')

