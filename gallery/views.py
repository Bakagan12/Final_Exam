from django.shortcuts import render
from django.shortcuts import render, redirect
from . forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
import requests

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
         return redirect("/")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print("Logged In")
                messages.info(request,f"You are now logged in as{username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,template_name="auth/login.html", context={"login_form":form})

def home(request):
    return render(request, "home.html",{})
def aboutus(request):
    return render(request, "aboutUs.html",{})
def contactus(request):
    return render(request, "contactUs.html",{})
def service(request):
    return render(request, "services.html",{})

def logout_request(request):
    logout(request)
    return redirect("/")

def register_request(request):
    if request.user.is_authenticated:
         return redirect("/")

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
              user = form.save()
              login(request, user)
              messages.success(request, "Registration Successful")
              return redirect("/")
        messages.error(request,"Registration Unsuccesful")
    form = NewUserForm()
    return render(request=request, template_name="auth/register.html", context={"register_form":form})

def albums(request):
    res_album = requests.get("https://jsonplaceholder.typicode.com/albums/")
    image_data= res_album.json()
    context = {
        'photos': image_data,
    }
    
    return render(request, "albums/index.html",context)


def photos(request, id):
    res_photos = requests.get("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id))
    photos = res_photos.json()

    res_album = requests.get("https://jsonplaceholder.typicode.com/albums/" + str(id))
    album = res_album.json()

    return render(request, "albums/photos.html", {
        'album': album,
        'photos': photos
    })