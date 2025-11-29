from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, UserProfile, Author, Book, Library, Librarian
)

# ---------------------------
# Custom User Admin
# ---------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_of_birth")
    
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

# ---------------------------
# Register Models
# ---------------------------
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
