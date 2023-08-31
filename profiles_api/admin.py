from django.contrib import admin

from profiles_api import models


#Built-in admin interface allows me to manage my app data through a user friendly interface
#I can register my models in this admin.py file to create, update and delete records
#from the admin interface without writing custom views
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)