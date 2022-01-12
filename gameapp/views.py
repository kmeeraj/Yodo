from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from gameapp.forms import LoginForm, ApplyForm
from django.contrib.auth import authenticate
from gameapp.models import LongitudeLatitude
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. ")


def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "../templates/hello.html", {"today" : today})

def list(request):
    longlat = LongitudeLatitude.objects.all
    print('request.user',request.user)
    if request.user.is_superuser:
      return render(request, '../templates/longitude.html', {"object_list" : longlat})
    else:
      return  HttpResponse("Hello, world, you cannot access this page ")



def login(request):
   username = "not logged in"

   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      print('is_valid', MyLoginForm.is_valid())
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         password = MyLoginForm.cleaned_data['password']
         print('username', username)
         dbuser = authenticate(username=username, password=password)
         print('dbuser',dbuser)
         if dbuser:
            username = dbuser
         else:
            MyLoginForm = LoginForm()
   else:
      MyLoginForm = LoginForm()

   if request.user.is_superuser:
      return render(request, '../templates/loggedin.html', {"username" : username})
   else:
      return redirect(hello)


def apply(request):
   username = "not logged in"

   if request.method == "POST":
      #Get the posted form
      MyApplyForm = ApplyForm(request.POST)
      print('is_valid', MyApplyForm.is_valid())
      if MyApplyForm.is_valid():
        longitude = MyApplyForm.cleaned_data['longitude']
        latitude = MyApplyForm.cleaned_data['latitude']
        username = MyApplyForm.cleaned_data['username']
        print('longitude', longitude)
        longlat = LongitudeLatitude(name = username, longitude = longitude, latitude = latitude)
        longlat.save()
        objects = LongitudeLatitude.objects.all()
        res ='Printing all LongitudeLatitude entries in the DB : <br>'
        for elt in objects:
          res += elt.name+"<br>"

   return redirect('/list/')


