
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from core.forms import RegisterForm, TechStackForm
from core.models import Technology, UserTechStack



# Authentication Views
class UserLoginView(LoginView):     # View for Signing In
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
    
    def get_form(self, form_class=None):
        form = super(UserLoginView, self).get_form(form_class)
        # Add class and placeholder to form fields
        form.fields['username'].widget = forms.TextInput(attrs={'class':'input-field','placeholder': 'Username'})
        form.fields['password'].widget = forms.TextInput(attrs={'class':'input-field','placeholder': 'Password'})
        return form


class UserSignupView(FormView):     # View for SignUp
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')    # Redirect to login after successful signup
    template_name = 'authentication/signup.html'
    
    def form_valid(self, form):     # Check if form is valid
        username = form.data['username']
        email = form.data['email']
        password = make_password(form.data['password'])
        User.objects.create(username=username, email=email, password=password)     # Save new user instance
        return super(UserSignupView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = 'user_login'    # Redirection after logout



# Core Views
class HomePage(ListView):       # View for retrieving current user's records
    model = UserTechStack
    template_name = 'core/home.html'
    
    def get_queryset(self):
        queryset = UserTechStack.objects.filter(user=self.request.user)
        return queryset


class AddTechStack(CreateView):     # View for adding new record
    model = UserTechStack
    template_name = 'core/form.html'
    form_class = TechStackForm
    
    def get_context_data(self, **kwargs):
        context = super(AddTechStack,self).get_context_data(**kwargs)
        context['add_page'] = True
        return context
    
    def form_valid(self, form):     # Check if form is valid
        form.instance.user = self.request.user  # save user's instance
        return super(AddTechStack, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home_page')    # Redirect to home page


class UpdateTechStack(UpdateView):      # View for updating a record
    model = UserTechStack
    template_name = 'core/form.html'
    form_class = TechStackForm
    
    def get_success_url(self):
        return reverse_lazy('home_page')    # Redirect to home page


class DeleteTechStack(DeleteView):      # View for deleting a record
    model = UserTechStack
    template_name = 'core/delete.html'
    
    def get_success_url(self):
        return reverse_lazy('home_page')    # Redirect to home page


class LoadTechnologies(View):       # View for getting technologies
    def get(self, request):
        category = request.GET.get('category')  # Get category Id
        technologies = Technology.objects.filter(category__id=category)     # Get technologies under the category
        return render(request, 'ajax/load_technologies.html', {'technologies': technologies})
