
from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import *

urlpatterns = [
    # Authentication URLs
    path('login', UserLoginView.as_view(), name='user_login'),
    path('signup', UserSignupView.as_view(), name='user_signup'),
    path('logout', UserLogoutView.as_view(), name='user_logout'),
    
    # Home URLs
    path('', login_required(HomePage.as_view()), name='home_page'),     # View URL
    path('add_techstack', login_required(AddTechStack.as_view()), name='add_techstack'),    # Create URL
    path('update_techstack/<int:pk>', login_required(UpdateTechStack.as_view()), name='update_techstack'),  # Update URL
    path('delete_techstack/<int:pk>', login_required(DeleteTechStack.as_view()), name='delete_techstack'),  # Delete URL
    
    # Ajax URL
    path('load_technologies', login_required(LoadTechnologies.as_view()), name='load_technologies'),
]
