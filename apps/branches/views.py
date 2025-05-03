from django.shortcuts import render
from .models import Branches

# Create your views here.
def branches_list (request):
    branches = Branches.objects.all()
    return render(request, 'branches/index.html', {'branches':branches})