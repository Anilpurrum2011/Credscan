from django.contrib import admin
# from django.contrib.auth.models import User, Group

# admin.site.register(User)
# admin.site.register(Group)

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Unregister the default User and Group admin classes
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your custom admin classes (if any)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    pass