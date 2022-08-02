import imp
from asyncio.windows_events import NULL
from pydoc import doc
from tkinter.messagebox import NO

from bson import is_valid
from cv2 import log
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginUser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import HttpResponse, redirect, render
from requests import request

from app.forms import TODOForm
from app.models import TODO


# Create your views here.
@login_required(login_url='loginpage')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request, 'index.html', context={'form':form, 'todos':todos})
        # return HttpResponse ("response from view file")
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            passwd =  form.cleaned_data.get('password')
            user = authenticate(username=user , password=passwd)
            print("authenticated", user)
            if user is not None:
                loginUser(request , user)
                return redirect('homepage')
        else:
            context = {
            "form":form
            }
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST) 
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('loginpage')   
        else:
            return render(request, 'signup.html', context=context)
@login_required(login_url='loginpage')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("homepage")
        else: 
            return render(request, 'index.html',context={'form':form})
        
@login_required(login_url='loginpage')
def signout(request):
    logout(request)
    return redirect("loginpage")
    
def delete_todo(request,id):
    TODO.objects.get(pk = id).delete()
    return redirect("homepage")

def change_status(request,id,status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect("homepage")
