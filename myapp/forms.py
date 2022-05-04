from django import forms
from django.forms import ModelForm

from .models import Consent, NjConsentData

from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    value = datetime.now().strftime("%d-%m-%Y")

class ConsentForm(ModelForm):

    class Meta:
        model = Consent
        fields = ['work_location', 'first_name', 'last_name', 'birth_date', 
        'address1', 'address2', 'zip_code', 'city', 'state', 'phone_no', 'email', 'gender', 'race', 'hispanic_latino','signature_name', 'date']
        widgets = {
            'birth_date': DateInput(),
            'gender': forms.RadioSelect,
            'race': forms.RadioSelect,
            'hispanic_latino': forms.RadioSelect,
            'date': DateInput(),
        }


class NjConsentForm(ModelForm):
    class Meta:
        model = NjConsentData
        fields = ['first_name', 'last_name', 'gender', 'school_name', 'race', 'ethnicity', 'test_taker_dob',
                  'address1', 'address2', 'zip_code', 'city', 'state', 'phone_no', 'email', 'consenter_type',
                  'school_district', 'school_county',  'signature_name', 'date']
        widgets = {
            'test_taker_dob': DateInput(),
            'gender': forms.RadioSelect,
            'race': forms.RadioSelect,
            'ethnicity': forms.RadioSelect,
            'date': DateInput(),
        }