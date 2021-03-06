from django.dispatch 			import receiver
from django.db.models.signals 	import post_save
from django.db 					import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	'''
		Tag Model
	'''
	name		= models.CharField(max_length=15, unique=True)

	def __str__(self):
		return self.name


class Diary(models.Model):
	'''
		Diary Model
	'''
	author 		= models.ForeignKey(User)
	title		= models.CharField(max_length=50)
	text 		= models.TextField()
	created_at	= models.DateTimeField(auto_now_add=True)
	tags		= models.ManyToManyField(Tag)

	def __str__(self):
		return self.title


class UserProfile(models.Model):
	'''
		Profile Model for User
	'''
	class Meta:
		verbose_name 		= "User profile"
		verbose_name_plural = "User's profiles"

	user 	  		= models.OneToOneField(User, primary_key=True)
	birthdate 		= models.DateField(null=True)
	friends   		= models.ManyToManyField('self', related_name="user_friends", symmetrical=False, through="Friendship", through_fields=("user1","user2"))
	notifications   = models.ManyToManyField('self', related_name="user_notifications",symmetrical=False, through="UserNotification")

	def __str__(self):
		return self.user.get_full_name()

# Get or create profile when try access to profile user (user.profile)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_profile_when_user_is_created(sender, instance, created, *args, **kwargs):
	if created:
		up = UserProfile.objects.create(user=instance)



class TypeNotification(models.Model):
	'''
		TypeNotification Model
	'''
	name 			  = models.CharField(max_length=15)

class Notification(models.Model):
	'''
		Notification Model
	'''
	emitter			  = models.ForeignKey(UserProfile)
	type_notification = models.ForeignKey(TypeNotification)
	diary			  = models.ForeignKey(Diary, null=True)


class UserNotification(models.Model):
	'''
		Notification Model
	'''
	receptor 			= models.ForeignKey(UserProfile)
	notification 		= models.ForeignKey(Notification)
	created_at			= models.DateTimeField(auto_now_add=True)
	class Meta:
		unique_together = (("receptor", "notification"),)


class Friendship(models.Model):
	'''
		Friendships model
	'''
	user1 	  	= models.ForeignKey(UserProfile, related_name="relation_source")
	user2 		= models.ForeignKey(UserProfile, related_name="relation_target")
	created_at	= models.DateTimeField(auto_now_add=True)
	class Meta:
		unique_together = (("user1", "user2"),)


class DiaryComment(models.Model):
	'''
		Comment for Diary Model
	'''
	diary 		= models.ForeignKey(Diary)
	text 		= models.TextField()
	author		= models.ForeignKey(User)

	def __str__(self):
		return self.text


class DiaryVote(models.Model):
	'''
		Vote for Diary Model
	'''
	diary 		= models.ForeignKey(Diary)
	author		= models.ForeignKey(User)

	def __str__(self):
		return self.author