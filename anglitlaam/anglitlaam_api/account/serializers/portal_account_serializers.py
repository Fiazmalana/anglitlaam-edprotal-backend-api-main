from rest_framework import serializers
from ..models.portal_account_models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
