from django.contrib import admin
from mydiary.models import Diary, UserProfile, Friendship

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
	list_display = ('title','author', 'created_at')
	list_filter  = ['created_at']


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user','birthdate')

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('user1', 'user2')
	list_filter  = ('user1', 'user2')

admin.site.register(Diary, DiaryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Friendship, FriendshipAdmin)