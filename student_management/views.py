from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

def Home(request):

    return render(request, 'includes/home.html')

def Login(request):
    return render(request, 'includes/login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('home')
            elif user_type == '2':
                return HttpResponse('This is Stuff Pannel')
            elif user_type == '3':
                return HttpResponse('This is Student Pannel')
            else:
                #message
                return redirect('login')
        else:
            print('invalid cred')
    else:
        #message
        return render(request, 'includes/login.html')