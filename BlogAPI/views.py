from django.shortcuts import render
from BlogAPI import models
from rest_framework.response import Response
from rest_framework import status,viewsets
from BlogAPI import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from BlogAPI import permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CreateProfileViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CreateUserSerializer
	queryset = models.BlogAPIProfiles.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.EditOnlyOwnProifle,)



class UserLoginApiView(ObtainAuthToken):
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserPostViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.UserPostSerializer
	authentication_classes = (TokenAuthentication,)
	queryset = models.Posts.objects.all()
	permission_classes = (permissions.UpdateOnlyOwnPost,IsAuthenticatedOrReadOnly)
	def perform_create(self,serializer):
		serializer.save(user_key=self.request.user)