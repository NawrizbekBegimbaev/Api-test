from rest_framework import serializers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        # Implement your create method here
        return User.objects.create(**validated_data)

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
    
    def create(self, validated_data):
        # Implement your create method here
        return Calendar.objects.create(**validated_data)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        # Implement your create method here
        return Event.objects.create(**validated_data)


class InvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invites
        fields = '__all__'

    def create(self, validated_data):
        # Implement your create method here
        return Invites.objects.create(**validated_data)