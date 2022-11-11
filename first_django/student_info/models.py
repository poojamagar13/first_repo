from django.db import models

# Create your models here.
class Studentdetail(models.Model):
    username =models.CharField(max_length=100, blank=False, null=False)
    password =models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    emailid = models.EmailField(default=True)

    class Meta:
        db_table = "studentdetail"
