from django.contrib import admin
from authentication.models import CustomUser

class UserAdmin(admin.ModelAdmin):
	list_display=('username','email','gender','civility','province','birth_year','profile_photo')
admin.site.register(CustomUser,UserAdmin)