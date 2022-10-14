from django.shortcuts import render, redirect
from .models import User
import bcrypt

def index(request):
    try:
        context= {
            'users':User.objects.all(),
            'loggedInUser':request.session['user']
        }
    except:
        context= {
            'users':User.objects.all(),
            'loggedInUser': 'no user logged in'
        }

    return render(request,'userApp/index.html',context)

def login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user'] = request.POST['email']
    except:
        print("you are stupid")

    return redirect("/userApp/")

def register(request):
    #errors = User.objects.basic_validator(request.POST)
    
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        )
        
    return redirect("/userApp/")

def logout(request):
    request.session.clear()
    return redirect('/userApp/')

def deleteUser(request,email):
    User.objects.get(email=email).delete()
    return redirect('/userApp/')