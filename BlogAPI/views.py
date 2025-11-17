from django.shortcuts import render
from BlogAPI import models
from rest_framework.response import Response
from rest_framework import status,viewsets
from BlogAPI import serializers

class CreateProfileViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CreateUserSerializer
	queryset = models.BlogAPIProfiles.objects.all()