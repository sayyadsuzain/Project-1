from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to dashboard
def home_redirect(request):
    return redirect('authentication:dashboard')

urlpatterns = [
    path('', home_redirect, name='home'),  # Redirect root URL to dashboard
    path('admin/', admin.site.urls),  # Admin interface
    path('registration/', include('registration.urls')),  # Registration app
    path('auth/', include('login_logout.urls')),  # Login/Logout app
    path('authentication/', include('authentication.urls')),  # Authentication app
]
