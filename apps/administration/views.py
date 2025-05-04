from django.shortcuts import render
from .models import Branches, Members

# Branches Index
def branches_index (request):
    #get all branch
    branches = Branches.objects.all()

    #render
    return render(request, 'branches/index.html', {'branches':branches})

# Members Index
def members_index (request):
    members = Members.objects.all()
    return render(request, 'members/index.html', {'members':members})