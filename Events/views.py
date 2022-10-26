
from email.headerregistry import ContentTransferEncodingHeader
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def get_home(request):
    return render(request, "home.html")


def get_login(request):
    return
# def get_nav(request):
#     return render(request, "navbar.html")


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("events/")
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "registration/register.html", context)


def get_event(request):
    events = Event.objects.all()
    context = {
        "events": events

    }
    return render(request, "Events.html", context)
