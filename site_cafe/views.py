from django.shortcuts import render
from .models import Category, Dish
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
    form = ReservationForm()
    return render(request, 'booking.html', {'form': form})

from .forms import ReservationForm
from .models import Reservation
class Book(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'booking.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        form.instance.processing = True
        return super().form_valid(form)

def registration(request):
    return render(request, 'registration.html')

def menu(request):
    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')
    return render(request, 'menu.html', {'categories': categories, 'dishes': dishes})
