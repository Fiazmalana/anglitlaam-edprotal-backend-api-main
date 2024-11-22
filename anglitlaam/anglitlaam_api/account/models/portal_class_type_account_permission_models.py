# models/portal_class_type_permission_models.py
from django.db import models

class ClassTypeAccountPermission(models.Model):
    account_id = models.IntegerField()
    class_type_id = models.IntegerField()
    is_allowed_to_teach = models.BooleanField(default=False)
    max_classes_per_day = models.IntegerField()
    class_type_account_permission_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'class_type_account_permission'  
    def __str__(self):
        return f"Account {self.account_id} - Class Type {self.class_type_id}"
