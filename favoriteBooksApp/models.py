from django.db import models
from userApp.models import User

# Their is no validation for the Books Form yet!!! Needs to be implemented!!
# The prinzip of validation should be  the same as in the userApp.models.py

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user_who_liked = models.ManyToManyField(User, related_name ="fav_books")
    created_by = models.CharField(max_length = 255, null = True)
    created_at = models.DateField(auto_now_add = True, null= True)
    updated_at = models.DateField(auto_now = True,null= True)

