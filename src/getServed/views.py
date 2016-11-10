from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from .models import SignUpForm, UploadRestaurantForm, LoginForm, User
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, "home.html", {})

def badLogin(request):
    return render(request, "js_passwordFailed.html", {})
		
def badName(request):
    return render(request, "js_usernameFailed.html", {})
		
def searchResult(request):
    return render(request, "searchResult.html", {})
		
def restProfile(request):
    return render(request, "restProfile.html", {})

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)

            instance.save()

            return render(request, "home.html", {})
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form': form})


def submit(request):
    form = UploadRestaurantForm()

    return render(request, "submit.html", {'form': form})


def login(request):

    if request.method == "POST":

        form = LoginForm(request.POST, request.FILES)

        if form.is_valid():

            user_form = form.clean_username()
            try:
                obj = User.objects.get(username=user_form)

                if obj.password != form.clean_password():
                    return render(request, "js_passwordFailed.html")
                else:
                    return render(request, "home.html", {})

            except ObjectDoesNotExist:
                messages.error(request, "The username was not found")

    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form})
