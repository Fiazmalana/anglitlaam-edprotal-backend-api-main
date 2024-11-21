from django.urls import path
from ..views.portal_account_forget_views import ForgetUsernameAPIView

urlpatterns = [
    path('', ForgetUsernameAPIView.as_view(), name='forget_username_api'),   
]
