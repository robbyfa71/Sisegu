from django.db import models
from django.db.models import SET_NULL
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.conf import settings

# Tier Mapping
class Tier(models.IntegerChoices):
    SISWA_M1 = 1, 'Siswa Melati 1'
    SISWA_M2 = 2, 'Siswa Melati 2'
    SISWA_M3 = 3, 'Siswa Melati 3'
    SISWA_M4 = 4, 'Siswa Melati 4'
    KADER_D = 5, 'Kader Dasar'
    KADER_M1 = 6, 'Kader Muda'
    KADER_M2 = 7, 'Kader Madya'
    KADER_M3 = 8, 'Kader Kepala'
    KADER_M4 = 9, 'Kader Utama'
    PENDEKAR_M1 = 10, 'Pendekar Muda'
    PENDEKAR_M2 = 11, 'Pendekar Madya'
    PENDEKAR_M3 = 12, 'Pendekar Kepala'
    PENDEKAR_M4 = 13, 'Pendekar Utama'
    PENDEKAR_M5 = 14, 'Pendekar Besar'

# Branches Model.
class Branches(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    phone_number = PhoneNumberField(region='ID') # Indonesia
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null = True)

    def __str__(self):
        return self.name #menampilkan nama


# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True)
    tier = models.IntegerField(choices=Tier.choices, default=Tier.SISWA_M1)
    years_of_joining = models.CharField(max_length=4, null=False, blank=False)




