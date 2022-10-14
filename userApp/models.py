from enum import unique
from statistics import mode
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'enter a valid email'
        if not (postData['password']) == postData['confirmPassword']:
            errors['password'] = 'password and ConfirmPassword are not the same'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250, primary_key = True)
    password = models.CharField(max_length = 250)
    objects = UserManager()

