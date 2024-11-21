# E:\anglitlaam-edprotal-backend-api-main\anglitlaam\anglitlaam_api\account\serializers\portal_class_type_serializers.py

from rest_framework import serializers
from ..models.portal_class_type_models import ClassType

class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = '__all__'

    def validate_class_duration_in_minutes(self, value):
        """Validate that class duration is a positive number"""
        if value <= 0:
            raise serializers.ValidationError("Class duration must be a positive integer.")
        return value

    def validate_class_charges_in_credit(self, value):
        """Validate that charges are not negative"""
        if value < 0:
            raise serializers.ValidationError("Class charges cannot be negative.")
        return value
