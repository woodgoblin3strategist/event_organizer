from datetime import datetime, timedelta
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from project_event.api.serializers import EventSerializer, ProjectSerializer
from project_event.models import Project, Event



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    @action(methods=['get'], detail=False)
    def time(self, request):
        queryset = super().get_queryset()

        try:
            start_date = datetime.strptime(self.request.query_params.get('start_date'), '%Y-%m-%d').date()
            end_date = datetime.strptime(self.request.query_params.get('end_date'), '%Y-%m-%d').date()
            if queryset.filter(is_owl_mode=False):
                end_date = end_date + timedelta(days=1)
            else:
                start_date = start_date - timedelta(days=1)
        except:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        if start_date or end_date:
            queryset = queryset.filter(
                Q(start_date__range=(start_date, end_date)) |
                Q(end_date__range=(start_date, end_date))
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
