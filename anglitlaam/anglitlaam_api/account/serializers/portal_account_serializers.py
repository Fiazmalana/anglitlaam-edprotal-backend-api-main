from rest_framework import serializers
from ..models.portal_account_models import Account

class AccountSerializer(serializers.ModelSerializer):
    account_type_key = serializers.CharField(source='account_type_id.account_type_key', read_only=True)
    account_type_display_name = serializers.CharField(source='account_type_id.account_type_display_name', read_only=True)

    class Meta:
        model = Account
        fields = '__all__'
