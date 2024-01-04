from django.contrib.auth import views as auth_views
from django.template.base import kwarg_re
from django.urls import path
from .views import LogoutView
from django.urls import path

from .views import DashboardView, UserRegistration


urlpatterns = [
   
    
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('register/', UserRegistration.as_view(), name='user-registration'),
]
