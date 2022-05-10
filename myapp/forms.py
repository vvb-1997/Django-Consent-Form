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
    authorize_checkbox = forms.BooleanField(required=True, label="""By completing and submitting this form, I confirm that I authorize the collection of specimens necessary to conduct COVID-19 testing on me during work hours or in connection with office attendance and work activity. I understand that authorizing COVID-19 testing is optional and that I can refuse to give this authorization, in which case, I will not be tested. COVID-19 screening testing will be conducted using a pooled PCR testing method. Screening testing will be conducted by a contracted vendor or company personnel. Any needed confirmatory or “follow-up” testing will be conducted by diagnostic PCR testing of the original specimen. TITANIQUE and testing provider, Mirimus, Inc., will maintain a copy of this consent form according to existing state and federal records retention laws and will only provide COVID-19 testing to individuals who have a completed consent form on file.""") 
    specimen_collection_checkbox = forms.BooleanField(required=True, label="""I authorize the collection of specimens to conduct pooled COVID-19 tests on me as part of a COVID-19 screening testing program. I understand this test will be provided at no cost to me. I understand that aggregate pooled test results for any pool of which I am a member will be reported to designated work personnel, and may be reported to me and to my state department of health (without identifying information). If I am a member of a pool that returns a positive result, I authorize a diagnostic PCR test of the original specimen to conduct individual follow-up tests on me. I understand this additional testing will be provided at no cost to me. I understand that my individual test result will be reported to designated company personnel and me, and will be reported to my state department of health, in accordance with state law. In the event I show symptoms of COVID-19 while at my office or am identified as a close contact to a person confirmed to have COVID-19, I authorize the administration of COVID-19 testing on me. I understand this testing will be provided at no cost to me. I understand that my test result will be available to designated company personnel and me, and will be reported to my state department of health, in accordance with state law. I authorize the testing provider, Mirimus, Inc., to securely maintain all legally required data collected from this consent form for test collection, processing, resulting, and reporting of specimens collected and tested during the duration of this testing program and according to existing state and federal records retention laws. By completing this consent form, I agree to have my test result emailed to the email address I provided in this form. I acknowledge that email communication is not a secure form of communication. I hereby waive any liability related to the transmission of my test results via email.l of the above.""") 
    
    class Meta:
        model = NjConsentData
        fields = ['first_name', 'last_name', 'gender', 'school_name', 'race', 'ethnicity', 
                  'address1', 'address2', 'zip_code', 'city', 'state', 'phone_no', 'email', 'consenter_type',
                  'school_district', 'school_county', 'date']
        widgets = {
            'test_taker_dob': DateInput(),
            'gender': forms.RadioSelect,
            'race': forms.RadioSelect,
            'ethnicity': forms.RadioSelect,
            'date': DateInput(),
        }
        