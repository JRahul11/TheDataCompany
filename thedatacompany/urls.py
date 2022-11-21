
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # Admin Panel URL
    path('admin/', admin.site.urls),
    
    # Google Authentication URLs
    path('accounts/', include('allauth.urls')),
    
    # Core App URLs
    path('', include('core.urls')),
]
