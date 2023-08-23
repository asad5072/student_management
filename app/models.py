from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER =(
        (1, 'HOD'),
        (2, 'STUFF'),
        (3, 'STUDENT'),
    )
    
    user_type = models.CharField(choices=USER, max_length=58, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

# students course model
class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# students session model
class Session_Year(models.Model):
    session_start = models.CharField(max_length=100, blank=True, null=True)
    session_end = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.session_start

#students model
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    # gender = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + ''+ self.admin.last_name