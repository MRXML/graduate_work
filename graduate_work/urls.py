"""
URL configuration for graduate_work project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_cafe import views
from accounts.views import RegisterUser, Login, logout_user
from site_cafe.views import Book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('store/', views.store, name='store'),
    path('booking/', views.booking, name='booking'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('registration/', views.registration, name='registration'),
    path('menu/', views.menu, name='menu'),
    path('book', Book.as_view(), name='book'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
