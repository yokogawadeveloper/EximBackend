from django.contrib import admin
from .models import User
from rest_framework_simplejwt.token_blacklist import models
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin


# Register your models here.

class NewOutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ('is_staff', 'is_verified', 'is_active', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)


admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)
