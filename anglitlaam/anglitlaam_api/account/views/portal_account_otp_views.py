import random
import requests
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.portal_account_models import Account

class OTPAPIView(APIView):
    def post(self, request):
        # Get input parameters
        username = request.data.get('account_user_name')
        phone_number = request.data.get('account_phone_number')

        # Validate input
        if not username or not phone_number:
            return Response(
                {"error": "Both 'account_user_name' and 'account_phone_number' are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the user exists in the database
        try:
            account = Account.objects.get(account_user_name=username, account_phone_number=phone_number)
        except Account.DoesNotExist:
            return Response(
                {"error": "No account found for the provided username and phone number."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Generate a random OTP
        otp_code = random.randint(100000, 999999)

        # Render the OTP email using the template
        email_message = render_to_string('otp_template.html', {'otp_code': otp_code, 'username': username})

        # Prepare the email parameters
        email_data = {
            "to": account.account_email_address,
            "subject": "Your OTP Code",
            "message": email_message,
            "cc": [],
            "type": "html"
        }

        # Send the OTP to the user's email using your email API
        email_api_url = "http://127.0.0.1:8000/send-email"
        try:
            email_response = requests.post(email_api_url, json=email_data)
            if email_response.status_code == 200:
                return Response(
                    {
                        "message": "OTP generated and sent successfully to your email.",
                        "otp": otp_code,
                        "account_email": account.account_email_address
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Failed to send OTP email. Please try again."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as e:
            return Response(
                {"error": f"Error sending email: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
