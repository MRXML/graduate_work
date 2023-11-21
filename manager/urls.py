from django.urls import path
from .views import ReservationList, ReservationUpdate
app_name = 'manager'

urlpatterns = [
    path('reservation/list/', ReservationList.as_view(), name='reservation_list'),
    path('reservation/edit/<int:pk>/', ReservationUpdate.as_view(), name='edit'),
]