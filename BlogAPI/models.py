from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class BlogAPIProfilesManager(BaseUserManager):
	def create_user(self,username,first_name,last_name,email,password=None):
		if not username:
			raise ValueError("Every user MUST have username")
		email = self.normalize_email(email)
		user = self.model(username=username,first_name=first_name,last_name=last_name,email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,username,first_name,last_name,email,password):
		user = self.create_user(username,first_name,last_name,email,password)
		user.is_superuser = True 
		user.is_staff = True 
		user.save(using=self._db)
		return user

class BlogAPIProfiles(AbstractBaseUser,PermissionsMixin):
	username = models.CharField(max_length=50,unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'username' 
	REQUIRED_FIELDS = ['first_name','last_name','email']

	def get_full_name(self):
		return self.first_name + self.last_name

	def get_short_name(self):
		return self.first_name

	def __str__(self):
		return self.email
