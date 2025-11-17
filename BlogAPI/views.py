from django.shortcuts import render
from BlogAPI import models
from rest_framework.response import Response
from rest_framework import status,viewsets
from BlogAPI import serializers
from rest_framework.authentication import TokenAuthentication
from BlogAPI import permissions

class CreateProfileViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CreateUserSerializer
	queryset = models.BlogAPIProfiles.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.EditOnlyOwnProifle,)