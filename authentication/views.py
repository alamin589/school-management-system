from django.shortcuts import render, redirect
from .models import User
from django.db.models import Q
from django.views import generic
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpResponse
from .forms import UserForm
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user-login')


class UserRegistration(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            # In a production system, you should hash the password before saving.
            form.save()
            return redirect('user-login')  # Correct the redirect URL
        return render(request, 'registration.html', {'form': form})

class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # In a production system, you should verify the password (e.g., by hashing and comparing).
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('dashboard')  # Correct the redirect URL
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})


class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'
    login_url = 'user-login'

