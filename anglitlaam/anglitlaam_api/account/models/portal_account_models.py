from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_first_name = models.CharField(max_length=255, null=True, blank=True)
    account_last_name = models.CharField(max_length=255, null=True, blank=True)
    account_user_name = models.CharField(max_length=255, null=True, blank=True)
    account_email_address = models.CharField(max_length=255, null=True, blank=True)
    account_phone_number = models.CharField(max_length=20, null=True, blank=True)
    account_type_id = models.IntegerField(null=True, blank=True)
    payment_account_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    account_date_of_birth = models.DateField(null=True, blank=True)  
    avatar_url = models.TextField(null=True, blank=True)   
    account_physical_address = models.TextField(null=True, blank=True)
    account_gender=models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'account'   
        managed = False  
    def __str__(self):
        return f"{self.account_first_name} {self.account_last_name} {self.account_email_address}"
