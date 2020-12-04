from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import forms,models
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.core.mail import EmailMessage
# Create your views here.


def login(request):
    if request.method=='POST':
        login_form=forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user=authenticate(username=login_name,password=login_password)
            if user is not None:
                auth.login(request,user)
                messages.add_message(request,messages.SUCCESS,'success login')
                return redirect('user:index')
            else:
                messages.add_message(request,messages.WARNING,'wrong name or password')
        else:
            messages.add_message(request,messages.WARNING,'please input right')
    else:
        login_form=forms.LoginForm()
    return render(request,'user/login.html',locals())

def index(request):
    if request.user.is_authenticated:
        username=request.user.username
        try:
            user=User.objects.get(username=username)
            diaries=models.Diary.objects.filter(user=user)
        except:
            pass
    messages.get_messages(request)
    return render(request,'user/index.html',locals())

def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO,'logout')
    return redirect('user:index')

@login_required(login_url='user/login.html')
def user_info(request):
    if request.user.is_authenticated:
        username=request.user.username
        try:
            user=User.objects.get(username=username)
            userinfo=models.Profile.objects.get(user=user)
        except:
            pass
    return render(request,'user/userinfo.html',locals())

@login_required(login_url='user/login.html')
def posting(request):
    if request.user.is_authenticated:
        username=request.user.username
        useremail=request.user.email
    messages.get_messages(request)

    if request.method=='POST':
        user=User.objects.get(username=username)
        diary=models.Diary.objects.get(user=user)
        post_form=forms.DiaryForm(request.POST,instance=diary)
        if post_form.is_valid():
            messages.add_message(request,messages.INFO,'saved')
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.WARNING,'wrong form')
    else:
        post_form=forms.DiaryForm()
        messages.add_message(request,messages.INFO,'add some thing')
    return render(request,'user/posting.html',locals())

def contact(request):
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            user_city=form.cleaned_data['user_city']
            user_school=form.cleaned_data['user_school']
            user_email=form.cleaned_data['user_email']
            user_message=form.cleaned_data['user_message']
            mail_body='''
            name:{}
            city:{}
            school:{}
            advice:{}
            
            '''.format(user_name,user_city,user_school,user_message)
            email=EmailMessage('advice from net',
                               mail_body,
                               user_email,
                               ['2975684744@qq.com'],
                               )
            email.send()
            messages.add_message(request,messages.INFO,'success')
        else:
            messages.add_message(request,messages.INFO,'failed')
    else:
        form=forms.ContactForm()
    return render(request,'user/contact.html',locals())