from django.utils import timezone
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Branches, Members, OutgoingMail, IncomingMail
from .forms import AddOutgoingMailForm

# Branches
@login_required
def branches_index (request):
    #get all branch
    branches = Branches.objects.all()
    return render(request, 'branches/index.html', {'branches':branches})

# Members
@login_required
def members_index (request):
    #get all members
    members = Members.objects.all()
    return render(request, 'members/index.html', {'members':members})


# mails
@login_required
def outgoingmails_index(request):
    #get all ougoing mails
    outgoingmails = OutgoingMail.objects.all()
    return render(request, 'outgoingmails/index.html',{'outgoingmails':outgoingmails})

@login_required
def outgoingmails_add(request):
    if request.method == 'POST':
        #get form data
        outgoingmail_form = AddOutgoingMailForm(request.POST)
        #check if form is valid
        if outgoingmail_form.is_valid():
            #save form data to database
            new_outgoingmail = outgoingmail_form.save(commit=False)
            new_outgoingmail.created_by=request.user
            new_outgoingmail.create_date = timezone.now()
            new_outgoingmail.save()
            #show success message
            messages.success(request,'Anda Berhasil Membuat Surat')
            return redirect('administration:outgoingmails_index')
        else:
            messages.error(request, 'Form tidak valid. Periksa kembali input Anda.')
    else:
        outgoingmail_form = AddOutgoingMailForm()
            
    return render(request, 'outgoingmails/add_new.html',{'form': outgoingmail_form})

@login_required
def incomingmails_index(request):
    #get all ougoing mails
    incomingmails = IncomingMail.objects.all()
    return render(request, 'incomingmails/index.html',{'incomingmails':incomingmails})