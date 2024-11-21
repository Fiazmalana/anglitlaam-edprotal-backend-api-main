# E:\anglitlaam-edprotal-backend-api-main\anglitlaam\anglitlaam_api\account\urls\portal_class_type_urls.py

from django.urls import path
from ..views.portal_class_type_views import ClassTypeListCreate, ClassTypeRetrieveUpdateDestroy

urlpatterns = [
    path('', ClassTypeListCreate.as_view(), name='class_type_list_create'),  # List and create
    path('class-types/<int:pk>/', ClassTypeRetrieveUpdateDestroy.as_view(), name='class_type_retrieve_update_destroy'),  # Retrieve, update, or destroy
]
