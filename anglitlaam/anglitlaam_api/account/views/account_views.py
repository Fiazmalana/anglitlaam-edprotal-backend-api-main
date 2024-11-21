from rest_framework import viewsets
from ..models.portal_account_models import Account
from ..serializers.portal_account_serializers import AccountSerializer
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

