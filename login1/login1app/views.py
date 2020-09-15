from django.shortcuts import render
from login1app.forms import UserForm,UserProfileInfoForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'login1app/index.html')

@login_required
def special(request):
    return HttpResponse("you are logged in ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        use_form = UserForm(data=request.POST)
        pro_form = UserProfileInfoForm(data=request.POST)
        if use_form.is_valid() and pro_form.is_valid():
            user= use_form.save()
            user.set_password(user.password)
            user.save()

            profile=pro_form.save(commit=False)
            profile.user=user

            registered=True

        else:
            print(use_form.errors,pro_form.errors)
    else:
        use_form=UserForm()
        pro_form=UserProfileInfoForm()
    return render(request,'login1app/register.html',{'use_form':use_form,'pro_form':pro_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username='username',password='password')
        if user:
            if user.is_active():
                login(request,user)
                HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("not actibe")

        else:
            print("not a user")
            print("geting detiLS")
            print(username,password)
    else:
        return render(request,'login1app/login.html',{})
