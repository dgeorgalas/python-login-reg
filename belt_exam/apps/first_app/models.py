from django.db import models
import datetime


class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(postData['first_name']) < 3:
        #     errors["first_name"] = "First Name must be more than 2 characters"
        # if len(postData['last_name']) < 3:
        #     errors["last_name"] = "Last Name must be more than 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if(postData["password"] != postData['confirm_pw']):
            errors["password"] = "Passwords do not match" 
        # if (not bool(re.match('^[a-zA-Z]+$', postData['first_name']))):
        #     errors["first_name"] = "First name should consist of only letters"
        # if (not bool(re.match('^[a-zA-Z]+$', postData['last_name']))):
        #     errors["last_name"] = "Last name should consist of only letters"
        # if (not bool(re.match(r'(\w+[.l\w])*@(\w+[.])*\w+', postData['email']))):
        #     errors["email"] = "Email is not a valid format"
        return errors

class Users(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(2016-02-02)
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


class Quotes(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(Users, related_name="user_quote")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = QuotesManager()


