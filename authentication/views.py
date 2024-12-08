from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render  
@login_required(login_url='/auth/login/')  # Explicitly set login URL
def dashboard_view(request):
    return render(request, 'authentication/dashboard.html')