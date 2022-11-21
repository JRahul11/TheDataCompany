
from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import *

urlpatterns = [
    # Authentication URLs
    path('login', UserLoginView.as_view(), name='user_login'),
    path('signup', UserSignupView.as_view(), name='user_signup'),
    path('logout', UserLogoutView.as_view(), name='user_logout'),
    
    # Home URLs
    path('', login_required(HomePage.as_view()), name='home_page'),
]
