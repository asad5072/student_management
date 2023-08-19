
from django.contrib import admin
from django.urls import path, include
from .import views,hod_views,student_views,stuff_views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('', views.dologin, name='dologin'),
    # path('Hod/home', hod_views.home, name='home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
