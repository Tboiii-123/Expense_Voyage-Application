from django.contrib import admin

# Register your models here.
from .models import Profile, Trip,Upcoming,Review,Price



admin.site.register(Profile)

# admin.site.register(Itenerary)

admin.site.register(Trip)

admin.site.register(Upcoming)

admin.site.register(Review)

admin.site.register(Price)
