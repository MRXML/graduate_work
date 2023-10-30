from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class User_reg(UserCreationForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'id': 'name',
                                                                       'placeholder': 'Your Name',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'placeholder': 'Your Phone',
                                                                         'class': 'form-control',
                                                                         'id': 'phone',
                                                                         'data-rule': 'minlen:4',
                                                                         'data-msg': 'Please enter a valid phone: 0xxxxxxxxx'}))
    address = forms.CharField(label='address', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'id': 'name',
                                                                             'placeholder': 'Your address',
                                                                             'data-rule': 'minlen:4',
                                                                             'data-msg': 'Please enter at least 4 chars'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'id': 'password1',
                                                                                    'placeholder': 'password',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                     'id': 'password2',
                                                                                     'placeholder': 'confirm password',
                                                                                     'data-rule': 'minlen:4',
                                                                                     'data-msg': 'Please enter at least 4 chars'}))
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'address')