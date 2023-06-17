
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
media_url=settings.MEDIA_URL



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('userlist/',views.userlist),
    path('login/',views.login),
    path('adminhome/',views.adminhome),
    path('addcourse/',views.addcourse),
    path('courselist1/',views.courselist1),
    path('addbatch/',views.addbatch),
    path('studenthome/',views.studenthome),
    path('batchlist1/',views.batchlist1),
    path('batchlist2/',views.batchlist2),
    path('courselist2/',views.courselist2)
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
