from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.register,name='register'),
]
