from django.contrib import admin
from .models import Branches, Members, OutgoingMail, IncomingMail

# Branches Admin.
@admin.register(Branches)

class BranchesAdmin (admin.ModelAdmin):
    list_display=('name', 'phone_number')

# Memhers Admin.
@admin.register(Members)

class MembersAdmin(admin.ModelAdmin):
    list_display=('name', 'birth_date', 'tier', 'years_of_joining')


# mails admin
@admin.register(OutgoingMail)
class OutgoingMailAdmin(admin.ModelAdmin):
    list_display=('mail_type','mail_number', 'subject', 'created_by')
@admin.register(IncomingMail)
class IncomingMailAdmin(admin.ModelAdmin):
    list_display=('mail_type','mail_number', 'sender')