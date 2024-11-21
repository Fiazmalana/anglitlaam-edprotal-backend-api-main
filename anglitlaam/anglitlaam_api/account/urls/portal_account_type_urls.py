from django.urls import path
from account.views.portal_account_type_views import (
    AccountTypeListCreateView,
    AccountTypeRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', AccountTypeListCreateView.as_view(), name='account_type_list_create'),  # GET and POST
    path('<int:account_type_id>/', AccountTypeRetrieveUpdateDestroyView.as_view(), name='account_type_detail'),  # GET, PUT, DELETE
]
