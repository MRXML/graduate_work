from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class User_reg(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'id': 'Username',
                                                                       'placeholder': 'Your Name',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter your User name'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'id': 'password1',
                                                                                    'placeholder': 'Input password',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                     'id': 'password2',
                                                                                     'placeholder': 'Repeat password',
                                                                                     'data-rule': 'minlen:4',
                                                                                     'data-msg': 'Please enter at least 4 chars'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')