from rest_framework import generics
from account.models import AccountType
from account.serializers.portal_account_type_serializers import AccountTypeSerializer

class AccountTypeListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all account types and creating a new account type.
    """
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer


class AccountTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a specific account type.
    """
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    lookup_field = 'account_type_id'  # Ensure it matches the primary key field
