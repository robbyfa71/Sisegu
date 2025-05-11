from django.utils import timezone
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from sisegu.apps.employee.administration.models import Branches, Members, OutgoingMail, IncomingMail
from .forms import AddOutgoingMailForm

# Landing Page
def index(request):
    return render(request, 'guest/index.html')
