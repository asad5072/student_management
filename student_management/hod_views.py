from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Session_Year, CustomUser
from django.contrib import messages
from app.models import *


@login_required(login_url=('/'))
def home(request):
    return render(request, 'Hod/home.html',)

@login_required(login_url=('/'))
def Add_sutdent(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        print(request.POST)
        profile_pic = request.FILES.get('student_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        class_name = request.POST.get('class_name')
        department_name = request.POST.get('department_name')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        class_roll = request.POST.get('class_roll')
        id_number = request.POST.get('id_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        do_brith = request.POST.get('do_brith')
        blood_group = request.POST.get('blood_group')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        # per_address = request.POST.get('pr_address')
        any_notes = request.POST.get('any_notes')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Taken.')
            return redirect('add_student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken.')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                profile_pic = profile_pic,
                user_type = 3,                
                email = email,               
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
                class_name = class_name,
                department_name = department_name,
                # course_name = course,
                class_roll = class_roll,
                id_number = id_number,
                fathers_name = fathers_name,
                mothers_name = mothers_name,
                do_brith = do_brith,
                blood_group = blood_group,
                mobile_number = mobile_number,
                address = address,
                # per_address = per_address,
                any_notes = any_notes,

            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + ' is Added Successfully!')
            return redirect('add_student')

    context= {
        'course': course,
        'session_year': session_year,
    }   
    return render(request, 'Hod/add_student.html', context)

# view student
def View_student(request):
    return render(request, 'Hod/view_student.html')

