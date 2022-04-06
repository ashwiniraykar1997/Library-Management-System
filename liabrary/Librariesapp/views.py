
from django.shortcuts import render,redirect
from django.urls import base, reverse

from django.http.request import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Librariesapp.models import books
from Librariesapp.forms import bookforms,auth_userforms


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Ashwini'})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        profile = request.POST['profile']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                #print('email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            #print('password not matching...')
            return redirect('register')

        return redirect('/')

    else:
        
        return render(request,'register.html')

        


def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             username = None
             if request.user.is_authenticated:
                username = request.user.username
                print("hi is current user",username)
                return redirect('book')
             else:
                 print('Please login into system first!!')
                 return redirect('login')
         else:
             messages.info(request,'invalid credentials please register first')
             return redirect('login')

   
      
    else:
        return render(request,'login.html')



def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Author = request.POST.get('Author')
        Quantity = request.POST.get('Quantity')

        print(name,price,Author,Quantity)

        b1 = books(name=name,price=price,Author=Author,Quantity=Quantity)
        b1.save()

        messages.success(request,'Record insert successfully')
        print('Record insert successfully')

        return redirect('display')
    
    return render(request,'book.html')

def display(request):
    result = books.objects.all()
    print(result)
    return render(request,'display.html',{'books':result})

def editbook(request,id):
    displaybook = books.objects.get(id=id)
    return render(request,"edit.html",{'books':displaybook})

def updatebook(request,id):
    updatebook = books.objects.get(id=id)
    form = bookforms(request.POST,instance=updatebook)

    if form.is_valid():
        form.save()

        messages.success(request,"Records Updated Successfully...!! ")
        #print("Records Updated Successfully...!!")

        return render(request,"edit.html",{'books':updatebook})


def deleterecord(request,id):
    delbook = books.objects.get(id=id)
    delbook.delete()
    result = books.objects.all()
   
    return render(request,'display.html',{'books':result})

def logout(request):
    auth.logout(request)
    return redirect('/')