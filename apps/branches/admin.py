from django.contrib import admin
from .models import Branches

# Register your models here.
@admin.register(Branches)

class BranchesAdmin (admin.ModelAdmin):
    list_display=('name', 'phone_number')