from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.

def signup(request):
    if request.method == "POST":
        # if request.POST['username'] in User:
        #     return redirect('index')

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user( username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
        
        else:
            context = {
                'error' : '비밀번호를 동일하게 입력하세요!'
            }
            return render(request, 'signup.html',context)
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            context = {
                'error' : '없는 계정!'
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')