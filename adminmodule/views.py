from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')
def emphomepage(request):
    return render(request,'emphomepage.html')
def customerhomepage(request):
    return render(request,'customerhomepage.html')

def signup(request):
    return render(request,'signup.html')

from django.contrib import messages
from django.contrib.auth.models import  User
def signup1(request):
    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists.')
                return render(request,'signup.html')
            else:
                user = User.objects.create_user(username,password=pass1)
                user.save()
                messages.info(request,'Account created Successfully!')
                return render(request,'projecthomepage.html')
        else:
            messages.info(request,'Password does not match.')
            return render(request,'signup.html')


def login(request):
    return render(request,'login.html')
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username) == 10:
                return redirect('customerhomepage')
            elif len(username) == 4:
                return redirect('emphomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.error(request, 'Invalid credentials')#error or info
            return render(request, 'login.html')
    else:
        return render(request,'login.html')


#from django.shortcuts import render, redirect
#from django.contrib import messages


def logout(request):
    auth.logout(request)
    return render(request,'projecthomepage.html')



