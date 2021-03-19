from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),   
    path('about', views.about, name='about'),   
    path('contact', views.contact, name='contact'),   
    path('search', views.search, name='search'),   
    path('signup', views.handlingSignup, name='handlingSignup'),
    path('login', views.handeLogin, name='handeLogin'),
    path('handeLogout', views.handeLogout, name='handeLogout'),

]