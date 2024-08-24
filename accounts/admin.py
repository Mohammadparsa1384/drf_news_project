from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":("job","bio")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields":("job","bio")}),
    )
