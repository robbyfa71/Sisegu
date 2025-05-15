from django import forms
from sisegu.apps.employee.administration.models import Branches, Members, OutgoingMail, IncomingMail


INPUT_CLASS = 'block w-full p-2 text-xs text-gray-900 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500'

class AddOutgoingMailForm(forms.ModelForm):
    class Meta:
        model = OutgoingMail
        fields = (
            'mail_type',
            'mail_number',
            'subject',
            'recipient',
            'event_name',
            'event_location',
            'event_Date', #perlu ubah Date menjadi date
            'signed_by',
            'signed_date',
            )
        widgets={
            'mail_type': forms.Select(attrs={
                'class':f"{INPUT_CLASS} mb-4",
                'id':'small',
                'name':'mail_type',
            }),
            'mail_number': forms.TextInput(attrs={
                'type':'text',
                'class': INPUT_CLASS,
                'id':'small-input',
                'name':'mail_number',
                'required':'required',
            }),
            'subject': forms.TextInput(attrs={
                'type':'text',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'subject',
                'required':'required',
            }),
            'recipient': forms.TextInput(attrs={
                'type':'text',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'recipient',
                'required':'required',
            }),
            'event_name': forms.TextInput(attrs={
                'type':'text',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'event_name',
            }),
            'event_location': forms.TextInput(attrs={
                'type':'text',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'event_location',
                'required':'required',
            }),
            'event_Date': forms.DateTimeInput(
                attrs={
                'type':'datetime-local',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'event_Date',
                'required':'required',
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'signed_by': forms.TextInput(attrs={
                'type':'text',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'signed_by',
            }),
            'signed_date': forms.TextInput(attrs={
                'type':'date',
                'class':INPUT_CLASS,
                'id':'small-input',
                'name':'signed_date',
            }),
        }
