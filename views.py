from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Example Django Rest Framework view
class ExampleViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for a demo API endpoint"""
    
    def list(self, request):
        # Sample data
        data = {
            'message': 'Hello from Django REST Framework!',
            'status': 'success'
        }
        return Response(data)

    def create(self, request):
        # Process the data from request.data
        return Response({'status': 'created'}, status=status.HTTP_201_CREATED)

# Example function-based API view
@api_view(['GET'])
def api_overview(request):
    """API Overview"""
    api_urls = {
        'List': '/example-list/',
        'Detail': '/example-detail/<str:pk>/',
        'Create': '/example-create/',
        'Update': '/example-update/<str:pk>/',
        'Delete': '/example-delete/<str:pk>/'
    }
    return Response(api_urls)
