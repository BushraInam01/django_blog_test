from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm

class SignupView(View):

    def get(self, request):
        form = SignupForm()

        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        return render(request, "accounts/signup.html", {"form": form})


#Login Views
class LoginView(View):

    def get(self, request):
        form = LoginForm()

        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("blog_list")

        return render( request, "accounts/login.html", {"form": form})

# Logout View
class LogoutView(View):

    def post(self, request):
        logout(request)

        return redirect("login")