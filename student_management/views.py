from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

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
                messages.error(request, 'Email or password is not match!')
                return redirect('login')
        else:
            print('invalid cred')
            messages.error(request, 'Email or password is not match! 222')
            return render(request, 'includes/login.html')
    else:        
        return render(request, 'includes/login.html')
    

def dologout(request):
    logout(request)
    return redirect('dologin')

def Profile(request):
    user = CustomUser.objects.get(id= request.user.id)
    print(user)
    context ={
        'user':user,
    }
    return render(request, 'includes/profile.html', context)

def Profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        usernme = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(profile_pic)

        try:
            customuser = CustomUser.objects.get(id= request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            # customuser.profile_pic = profile_pic

            if password !=None and password !='':
                customuser.set_password(password)
            if profile_pic !=None and profile_pic !="":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully!')
            return redirect('profile_update')
        except:
            messages.error(request, 'Failed to Update Your Profile!')

    return render(request, 'includes/profile.html')
