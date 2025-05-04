from django.contrib import admin
from .models import Branches, Members

# Branches Admin.
@admin.register(Branches)

class BranchesAdmin (admin.ModelAdmin):
    list_display=('name', 'phone_number')

# Memhers Admin.
@admin.register(Members)

class MembersAdmin(admin.ModelAdmin):
    list_display=('name', 'birth_date', 'tier', 'years_of_joining')