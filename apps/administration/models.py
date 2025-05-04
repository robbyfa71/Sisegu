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

# Mail type mapping
class MailType(models.IntegerChoices):
    UNDANGAN = 1, 'Undangan'
    SK = 2, 'Surat Keputusan'
    PERINTAH = 3, 'Surat Perintah'
    PERMOHONAN = 4, 'Surat Permohonan'
    PEMBERITAHUAN = 5, 'Surat Pemberitahuan'
    PROPOSAL = 6, 'Proposal'
    PEMINJAMAN= 7, 'Surat Peminjaman'


# Branches Model.
class Branches(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    phone_number = PhoneNumberField(region='ID') # Indonesia
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null = True)

    class Meta:
        verbose_name_plural="Branches"

    def __str__(self):
        return self.name #menampilkan nama


# members model
class Members(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True)
    tier = models.IntegerField(choices=Tier.choices, default=Tier.SISWA_M1)
    years_of_joining = models.CharField(max_length=4, null=False, blank=False)

    class Meta:
        verbose_name="Member"

    def __str__(self):
        return self.name #menampilkan nama


# mails model
class OutgoingMail(models.Model):
    mail_type = models.IntegerField(choices=MailType.choices, default=MailType.UNDANGAN)
    mail_number = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=150, blank=False)
    recipient = models.CharField(max_length=150, blank=True)
    event_name = models.CharField(max_length=150, blank=False)
    event_location = models.CharField(max_length=150, blank=True, )
    event_Date = models.DateTimeField(null=True, blank=True) # perlu ubah Date menjadi date
    signed_by=models.CharField(max_length=80, blank=False)
    signed_date=models.DateField(null=False, blank=False)
    created_date=models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural='Outgoing Mails'


    def __str__(self):
        return self.subject #menampilkan subjek surat

class IncomingMail(models.Model):
    mail_type = models.IntegerField(choices=MailType.choices, default=MailType.UNDANGAN)
    mail_number = models.CharField(max_length=50, blank=True)
    mail_purpose = models.TextField(blank=True)
    sender = models.CharField(max_length=150, blank=False)
    created_date=models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Incoming Mails'
    
    def __str__(self):
        return self.sender #menampilkan pengirim surat





