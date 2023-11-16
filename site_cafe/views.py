from django.shortcuts import render
from .models import Category, Dish

def main_page(request):
    category = Category.objects.filter(is_visible=True)
    return render(request, 'index.html', context={'category': category})


def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def store(request):
    return render(request, 'store.html')

def booking(request):
    return render(request, 'booking.html')

def registration(request):
    return render(request, 'registration.html')

def menu(request):
    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')
    return render(request, 'menu.html', {'categories': categories, 'dishes': dishes})