from django.urls import path
from views.portal_class_type_account_permission_views import ClassTypeAccountPermissionViewSet
from rest_framework.routers import DefaultRouter

# Initialize router and register the viewset
router = DefaultRouter()
router.register(r'class_type_account_permission', ClassTypeAccountPermissionViewSet)

# Add the URLs to urlpatterns
urlpatterns = router.urls
