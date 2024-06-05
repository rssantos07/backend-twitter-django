from django.contrib import admin
from usuario.models import User, Profile, Post

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    
class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name', 'verified']
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)    
admin.site.register(Post)
