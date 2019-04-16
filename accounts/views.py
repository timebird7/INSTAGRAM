from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('posts:list')
        else:
            return redirect('accounts:signup')
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
        
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:list')
        else:
            return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('posts:list')