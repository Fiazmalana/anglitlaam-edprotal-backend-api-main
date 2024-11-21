# E:\anglitlaam-edprotal-backend-api-main\anglitlaam\anglitlaam_api\account\views\portal_class_type_views.py

from rest_framework import generics
from ..models.portal_class_type_models import ClassType
from ..serializers.portal_class_type_serializers import ClassTypeSerializer

# List and Create ClassType entries
class ClassTypeListCreate(generics.ListCreateAPIView):
    queryset = ClassType.objects.all()  # Get all ClassType objects
    serializer_class = ClassTypeSerializer  # Serializer to use for responses


# Retrieve, Update, or Destroy ClassType entries by ID
class ClassTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassType.objects.all() 
    serializer_class = ClassTypeSerializer  
