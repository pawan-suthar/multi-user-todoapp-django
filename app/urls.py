from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path
from requests import request

from app.views import (addtodo, change_status, delete_todo, home, login,
                       signout, signup)

urlpatterns = [
    path('',home, name='homepage'),
    path('login', login, name='loginpage'), 
    path('signup', signup, name='signuppage'),
    path('add', addtodo, name='addtodo'),
    path('logout', signout,name='logout'),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_status),
] 
