from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'examples', views.ExampleViewSet, basename='example')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('', include(router.urls)),
]
