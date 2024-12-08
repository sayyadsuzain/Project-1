from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('auth:login')  # Redirect to login page after registration
        else:
            # If form is invalid, re-render the page with errors
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
