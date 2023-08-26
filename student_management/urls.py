
from django.contrib import admin
from django.urls import path, include
from .import views,hod_views,student_views,stuff_views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('', views.dologin, name='dologin'),
    path('', views.dologout, name='dologout'),
    
    path('profile/', views.Profile, name='profile'),
    path('profile/update', views.Profile_update, name= 'profile_update'),
    path('Hod/home', hod_views.home, name='hod_home'),
    path('hod/student/add_student', hod_views.Add_sutdent, name='add_student'),
    path('hod/student/view', hod_views.View_student, name='view_student'),
    path('hod/student/edit/<str:id>', hod_views.Edit_student, name='edit_student'),
    path('hod/student/update', hod_views.Update_student, name='update_student'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
