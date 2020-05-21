from django import forms
from payment.models import Donor

class DonorForm(forms.ModelForm):
    class Meta():
        model = Donor
        fields = ('name', 'city', 'email', 'amount')