from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=35)
    DOB = models.DateField(auto_now=False, null=True, blank=True)
    mobile = models.FloatField()
    email = models.EmailField()
    ID = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# class Organiser(models.Model):
#     user = models.OneToOneField(
#         User, 
#         on_delete = models.CASCADE,
#         primary_key = True,
#     )

#     company = models.CharField(max_length=35)
#     def __str__(self):
#         return self.user 