from django.db import models

class productManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors["name"] = "Name should be at least 2 characters"
        if len(postData['desc']) < 10 and postData['desc'] != "":
           errors["desc"] = "Description should be at least 10 characters if not empty"
        if len(postData['brand']) < 1:
            errors["brand"] = "Field cannot be empty"
        if len(postData['processor']) < 1:
            errors["processor"] = "Field cannot be empty"
        if len(postData['memory']) < 1:
            errors["memory"] = "Field cannot be empty"
        if len(postData['storage']) < 1:
            errors["storage"] = "Field cannot be empty"
        if len(postData['category']) < 1:
            errors["category"] = "Field cannot be empty"

        return errors

class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Processor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Memory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Graphics_card(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Storage(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=45)
    desc = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name="products", on_delete = models.CASCADE)
    processor = models.ForeignKey(Processor, related_name="products", on_delete = models.CASCADE)
    memory = models.ForeignKey(Memory, related_name="products", on_delete = models.CASCADE)
    graphics_card = models.ForeignKey(Graphics_card, related_name="products", on_delete = models.CASCADE, blank=True, null=True)
    storage = models.ForeignKey(Storage, related_name="products", on_delete = models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = productManager()

# class Accessory(models.Model):
#     name = models.CharField(max_length=45)
#     brand = models.CharField(max_length=45, blank=True, null=True)
#     desc = models.TextField()   
#     objects = accessoryManager()