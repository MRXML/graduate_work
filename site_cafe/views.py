from django.shortcuts import render
from .models import Category
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