from django.contrib.auth.models import User
from rest_framework import serializers
from project_event.models import Project, Event



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    events = EventSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = '__all__'
