from django.contrib import admin
from .models import User
from .models import Registration
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")

@admin.register(Registration)
class UserAdminReg(admin.ModelAdmin):
    list_display = ("id", 'child_name', 'child_age', 'child_dob', 'child_gender', 'mother_name', 'mother_age')
