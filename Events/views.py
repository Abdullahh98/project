from django.shortcuts import render,redirect
from Events.form import UserForm

# Create your views here.
def get_home(request):
    return render(request, "home.html")

def get_nav(request):
    return render(request, "navbar.html")


def create_user(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {
        "form": form
    }

    return render(request, "create_user.html", context)