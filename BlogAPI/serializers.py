from rest_framework import serializers
from BlogAPI import models

class CreateUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BlogAPIProfiles
		fields = ('id','username','first_name','last_name','email','password')
		extra_kwargs = {'password':{'write_only':True,'style':{'input_type':'password'}}}
	def create(self,validated_data):
		user = models.BlogAPIProfiles.objects.create_user(
			username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			email=validated_data['email'],
			password=validated_data['password']
			)
		return user

	def update(self,instance,validated_data):
		if 'password' in validated_data:
			password = validated_data.pop('password')
			instance.set_password(password)
			instance.save()
		return super().update(instance,validated_data)