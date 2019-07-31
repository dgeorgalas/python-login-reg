from __future__ import unicode_literals
from django.db import models

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) <= 1:
            errors["first_name"] = "First Name must be more than 2 characters"
        if len(postData['last_name']) <= 1:
            errors["last_name"] = "Last Name must be more than 2 characters"
        if len(postData['password']) <= 7:
            errors["password"] = "Password must be at least 8 characters"
        if(postData["password"] == postData['confirm_passwod']):
            errors["password"] = "Passwords do not match" 
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = UsersManager()


