# userauth/views.py

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomAuthenticationForm

class LoginView(View):
    form_class = CustomAuthenticationForm
    template_name = 'userauth/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('/')
