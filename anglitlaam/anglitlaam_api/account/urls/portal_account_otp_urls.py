from django.urls import path
from ..views.portal_account_otp_views import OTPAPIView

urlpatterns = [
    path('', OTPAPIView.as_view(), name='otp'),  # Use the base URL under this file
]
