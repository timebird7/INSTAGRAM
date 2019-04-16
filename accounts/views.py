from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user_model
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('posts:list')
        else:
            messages.success(request, 'not valid')
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
            messages.success(request, 'not valid')
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
    
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    posts = profile.post_set.all()
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'accounts/profile.html', context)
    
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    else:
        return render(request, 'accounts/delete.html')