from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from site_cafe.models import Reservation
from .forms import EditForm
from django.urls import reverse_lazy


class ManagerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='managers').exists()



class ReservationList(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy('login')
    model = Reservation
    template_name = 'book_list.html'
    context_object_name = 'reservations'

class ReservationUpdate(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    login_url = '/login/'
    model = Reservation
    form_class = EditForm
    template_name = 'edit.html'
    success_url = reverse_lazy('manager:reservation_list')

