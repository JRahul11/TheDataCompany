
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'input-field','placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class':'input-field','placeholder':'Email'}),
            'password': forms.TextInput(attrs={'class':'input-field','placeholder':'Password'}),
        }