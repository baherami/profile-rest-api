from django.contrib import admin

#import the model files
from . import models

# Register your models here.

#register the user profile model
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
