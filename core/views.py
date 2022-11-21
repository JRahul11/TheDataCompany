
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from core.forms import RegisterForm



class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_form(self, form_class=None):
        form = super(UserLoginView, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class':'input-field','placeholder': 'Username'})
        form.fields['password'].widget = forms.TextInput(attrs={'class':'input-field','placeholder': 'Password'})
        return form


class UserSignupView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        username = form.data['username']
        email = form.data['email']
        password = make_password(form.data['password'])
        User.objects.create(username=username, email=email, password=password)
        return super(UserSignupView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = 'user_login'


class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')