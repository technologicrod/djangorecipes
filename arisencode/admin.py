from django.contrib import admin
from .models import Profile, Recipe  # Import the Profile and Recipe models

admin.site.register(Profile)  # Register the Profile model
admin.site.register(Recipe)   # Register the Recipe model
