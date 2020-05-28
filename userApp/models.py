from django.db import models
import re

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):       
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Lirst Name should be at least 2 characters"
        if len(postData['pwd']) < 8:
            errors["pwd_length"] = "Password Must be 10 character long"
        if postData['pwd'] != postData['confirm_pwd']:
            errors["pwd"] = "Password Do Not Match"
        
        users = User.objects.all()
        for user in users:
            if postData['email'] == user.email:
                errors['email'] = "email is taken"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    products = models.ManyToManyField('productApp.Product', related_name="wishlists")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)