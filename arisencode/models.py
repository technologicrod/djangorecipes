from django.db import models

class Profile(models.Model):
    email = models.EmailField(unique=True, default='email@email.com')
    password = models.CharField(max_length=128, blank=True, null=True)
    account_type = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.name

class Login(models.Model):
    email = models.EmailField(unique=True, default='email@email.com')
    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.email
