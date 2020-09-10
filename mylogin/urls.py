from django.urls import path
from . import views

urlpatterns = [
     path('register/', views.registerPage, name="register"),
     path('', views.loginPage, name="login"),
     path('home/logout/', views.logoutUser, name="logout"),
     path('home/', views.home, name="home"),

]
