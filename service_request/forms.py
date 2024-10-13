from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'customer_email', 'service_type', 'details', 'attachment']


class TrackRequestForm(forms.Form):
    customer_email = forms.EmailField(label='Your Email')
    created_at = forms.DateField(label='Date of Request (YYYY-MM-DD)', widget=forms.TextInput(attrs={'type': 'date'}))
