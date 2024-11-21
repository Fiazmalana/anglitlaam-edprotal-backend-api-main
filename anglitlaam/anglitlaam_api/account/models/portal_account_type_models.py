from django.db import models

class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    account_type_key = models.CharField(max_length=100, unique=True)
    account_type_display_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'account_type'  

    def __str__(self):
        return self.account_type_display_name
