# E:\anglitlaam-edprotal-backend-api-main\anglitlaam\anglitlaam_api\account\models\portal_class_type_models.py

from django.db import models

class ClassType(models.Model):
    class_type_id = models.AutoField(primary_key=True)
    class_type_key = models.CharField(max_length=100)
    class_type_display_name = models.CharField(max_length=255)
    class_duration_in_minutes = models.IntegerField()
    class_charges_in_credit = models.DecimalField(max_digits=10, decimal_places=2)
    class_type_group_id = models.IntegerField()

    def __str__(self):
        return self.class_type_display_name

    class Meta:
        db_table = 'class_type'   
