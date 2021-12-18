from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from django.contrib import messages

from . import forms

User = get_user_model()
# Panel View

def index(request):
    return render(request, 'home/select-panel/index.html')

# def signin(request):
#     return render(request, 'home/signin/index.html')

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'home/signin/index.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("\n", email, "\n", password)
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                return redirect("home:profile")
            else:
                return HttpResponse('There is no such a user <a href="/">GO BACK</a>')
        else:
            messages.warning(request, "ایمیل یا رمز عبور نمیتواند خالی باشد.")
            return redirect("home:login")

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "home/profile/index.html")

    def post(self, request, *args, **kwargs):
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "اطلاعات شما با موفقیت تغییر یافت.")
            return redirect("home:profile")
        else:
            context = { "errors": form.errors }
            messages.error(request, "لطفا فرم اطلاعات را به درستی وارد کنید.")
            return render(request, "home/profile/index.html", context)




def profile(request):
    return render(request, 'home/profile/index.html')

def panel(request):
    return render(request, 'home/panel/index.html')