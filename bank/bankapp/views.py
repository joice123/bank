
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,logout,login


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:newform')
        else:
            messages.info(request, 'invalid')
            return redirect('bankapp:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, 'username already')
                return redirect('bankapp:register')
            elif User.objects.filter(password=password):
                messages.info(request, 'password already')
                return redirect('bankapp:register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                return redirect('bankapp:login')
        else:
            messages.info(request, 'incorect password')
            return redirect('bankapp:register')
        return redirect('/')

    return render(request, 'register.html')


def kottayam(request):
    return render(request, 'kottayam.html')


def alappuzha(request):
    return render(request, 'alappuzha.html')


def idukki(request):
    return render(request, 'idukki.html')


def ernakulam(request):
    return render(request, 'ernakulam.html')

def form(request):
    if request.method == 'POST':
            return redirect('confirmation')

    program = Programming.objects.all()
    d = {'program': program}
    return render(request,'form.html',d)

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})

def Logout(request):
    auth.Logout(request)
    return redirect('/')


def kannur(request):
    return render(request, 'kannur.html')


def newform(request):
    return render(request, 'sampleform.html')


def form(request):

    program = Programming.objects.all()
    d = {'program': program}
    return render(request, 'form.html', d)


def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})

def ok(request):
    return render(request,'confirm.html')