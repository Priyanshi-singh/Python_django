from django.shortcuts import render,redirect
from .forms import LoginForm , RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages   #to display messages and notifications


User = get_user_model()      # to get the user model


def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')

        #session management code
        user = authenticate(request, username = uname, password= pwd)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('/')
        #session management code end
    else:
        messages.error(request, 'Invalid Data')

    ctx={
            'form' : form,
            'titie' : 'Login|Blogist',
        }
    return render(request, "account/login.html",ctx)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1==password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('/')
        else:
            messages.success(request, "Password do not match")
    ctx = { 'form' : form , 'title': 'Register|Blogist'}
    return render(request, "account/register.html", ctx)
