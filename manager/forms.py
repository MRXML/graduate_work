from django import forms
from site_cafe.models import Reservation


class EditForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['processing', 'user_name', 'user_phone', 'user_datetime', 'user_count', 'special_requests', ]