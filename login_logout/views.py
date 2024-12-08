from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Django's built-in login form
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('authentication:dashboard')  # Redirect to the dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login_logout/login.html', {'form': form})  # Render the login page

# View for user logout
def logout_view(request):
    logout(request)
    return redirect('auth:login')  # Redirect to the login page after logout