from django import forms
from .models import WaitlistEmail, Contact
from django.core.validators import MinLengthValidator

class WaitlistForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control-custom", "placeholder": "Enter your email address"}))
    class Meta:
        model = WaitlistEmail
        fields = ['email']


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Name","class": "form-control","id":"full_name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Your Email", "class": "form-control ","id":"email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"id":"message","placeholder": "Leave us a message...."}), validators=[MinLengthValidator(15, message='Please enter at least 15 characters')])
    
    class Meta:
        model = Contact
        fields = ['full_name','email','message']