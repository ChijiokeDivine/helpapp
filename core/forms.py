from django import forms
from .models import WaitlistEmail

class WaitlistForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control-custom", "placeholder": "Enter your email address"}))
    class Meta:
        model = WaitlistEmail
        fields = ['email']