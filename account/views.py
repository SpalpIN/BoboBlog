from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:homepage')
