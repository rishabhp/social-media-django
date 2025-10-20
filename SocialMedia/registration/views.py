from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import ProfileImage

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data.get('profile_pic')
            user = form.save()
            if profile_pic is not None:
                ProfileImage.objects.create(image=profile_pic, user=user)
            else:
                print("hi")
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')