# serializers/portal_class_type_permission_serializers.py
from rest_framework import serializers
from models.portal_class_type_account_permission_models import ClassTypeAccountPermission

class ClassTypeAccountPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTypeAccountPermission
        fields = '__all__'  # or explicitly list fields like ['account_id', 'class_type_id', ...]
# 