from django.contrib import admin
from .models import Member, Author
from django.contrib.auth.admin import UserAdmin
# # Register your models here.
# admin.site.register(User)


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model= Member
    fieldsets= (
        (None, {'fields': ('username', 'password')}),
        ("Personal Info", {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_image', 'mobile')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Importants Dates", {"fields": ('last_login', 'date_joined')})
    )

    add_fieldsets= (
        (None, {
            'classes': ('wide'),
            'fields': ('username', 'password1', 'password2', 'email', 'mobile', 'bio', 'profile_image')
        })
    )

    list_display= ('username', 'first_name', 'last_name', 'email', 'mobile', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'mobile')


admin.site.register(Member, UserAdmin)
admin.site.register(Author)
    
