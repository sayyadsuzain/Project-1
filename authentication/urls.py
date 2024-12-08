from django.urls import path
from . import views

# Namespace for the authentication app
app_name = 'authentication'

# URL patterns for authentication app
urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard view
]
