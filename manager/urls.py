from django.urls import path
from .views import ReservationList
app_name = 'manager'

urlpatterns = [
    path('reservation/list/', ReservationList.as_view(), name='reservation_list'),
]