from django.db import models
from django.db.models import SET_NULL
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Branches(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    phone_number = PhoneNumberField(region='ID') # Indonesia
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null = True)

    def __str__(self):
        return self.name #menampilkan nama



