from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirmPassword')

        if pass1!=pass2:
            return HttpResponse('your password are not same!!!')
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username =request.POST.get("username")
        pass1 =request.POST.get("password")
        user=authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect!!!')

    return render(request, 'login.html')