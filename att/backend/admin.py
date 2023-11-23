from django.contrib import admin
from django.contrib.auth.models import User

from backend import models
# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = models.UserProfile

class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Class)
admin.site.register(models.Student)
admin.site.register(models.Semester)
admin.site.register(models.College_Day)
admin.site.register(models.Lecturer)
admin.site.register(models.Course)

# Register your models here.
