from django.urls import include, path
from rest_framework import routers
from project_event.api import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, basename='events')
router.register(r'projects', views.ProjectViewSet, basename='projects')


urlpatterns = [
    path('api/', include(router.urls)),
]

