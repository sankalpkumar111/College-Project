from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Custom admin class for Accountant
class AccountantAdmin(admin.ModelAdmin):
    pass  # You can customize this admin class if needed

# Register your models here.
class UserModel(UserAdmin):
    ordering = ('email',)

# Register models with their respective admin classes
admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Accountant, AccountantAdmin)  # Register Accountant model with the custom admin class
