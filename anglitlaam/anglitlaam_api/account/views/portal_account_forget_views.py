import requests
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.portal_account_models import Account
from django.db import connection

class ForgetUsernameAPIView(APIView):
    def post(self, request):
        # Get the phone number from the request
        phone_number = request.data.get('account_phone_number')

        # Validate input
        if not phone_number:
            return Response(
                {"error": "'account_phone_number' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Query to find account_type_id where account_type_key is 'STUDENT'
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT account_type_id FROM account_type WHERE account_type_key = %s", ['STUDENT']
            )
            result = cursor.fetchone()

        if not result:
            return Response(
                {"error": "No account type with key 'STUDENT' exists."},
                status=status.HTTP_404_NOT_FOUND,
            )

        student_account_type_id = result[0]

        # Query accounts matching the phone number and account_type_id
        accounts = Account.objects.filter(
            account_phone_number=phone_number,
            account_type_id=student_account_type_id
        )

        if not accounts.exists():
            return Response(
                {"error": "No student account found for the provided phone number."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Send an email to each user with their username
        for account in accounts:
            username = account.account_user_name
            email = account.account_email_address

            if not email:
                continue  # Skip if no email address is found for this account

            # Render email content for this specific username
            email_message = render_to_string('email_template.html', {'username': username})
            email_data = {
                "subject": "Username Retrieval",
                "to": email,
                "message": email_message,
                "type": "html"  
            }

            # Send email
            email_response = self.send_email(email_data)

            if not email_response or email_response.status_code != 200:
                return Response(
                    {"error": f"Failed to send email to {email}."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"message": "Usernames retrieved and emails sent successfully."},
            status=status.HTTP_200_OK,
        )

    def send_email(self, email_data):
        try:
            response = requests.post("http://127.0.0.1:8000/send-email", json=email_data)
            print(f"Email API response status: {response.status_code}")
            print(f"Email API response body: {response.text}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending email: {e}")
            return None
