from django.contrib import admin
from mydiary.models import Diary, UserProfile, Friendship, Tag

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
	list_display = ('title','author', 'created_at')
	list_filter  = ['created_at', 'tags__name']

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user','birthdate')

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('user1', 'user2', 'created_at')
	list_filter  = ('user1', 'user2', 'created_at')

class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Diary, DiaryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Tag, TagAdmin)