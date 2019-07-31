from __future__ import unicode_literals
from django.db import models
import datetime

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "Name must be at least 3 characters"
        if len(postData["email"]) < 3:
            errors["email"] = "Email must be at least 3 charactes"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if(postData["password"] != postData['confirm_pw']):
            errors["password"] = "Passwords do not match" 
        return errors

    def login_validator(self, postData):
        errors={}
        users = Users.object.filter(email=postData["email"])
        if users.exists():
            user = users[0]
            if postData["password"] == user.password:
                return errors
            else:
                errors["password"] = "Email and Password do not match"
        else:
            errors["email"] = "Email and Password do not match"
        return errors

        


class Users(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = UsersManager()


class QuotesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["quoted_by"]) < 4:
            errors["quoted_by"] = "Quoted by: more than 3 characters"
        if len(postData["message"]) < 11:
            errors["message"] = "Message: more than 10 characters"
        return errors


class Quotes(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(Users, related_name="user_quote")
    favorites = models.ManyToManyField(Users, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = QuotesManager()








