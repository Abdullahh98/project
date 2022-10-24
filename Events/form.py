from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meat:
        model = User
        fields = ["name","DOB","mobile","email","ID"]


# class OrganiserForm(forms.ModelForm):
#     class Meat:
#         model = Organiser
#         fields = ["name","DOB","mobile","email","ID","company"]