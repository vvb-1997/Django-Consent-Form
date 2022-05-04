from audioop import reverse
from django.shortcuts import render
from django.views.generic import CreateView
# from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Consent, NjConsentData
from .forms import ConsentForm, NjConsentForm
from .functions import send_email

# Create your views here.
def home(request):
    return render(request, "myapp/home.html",{})

class ConsentCreateView(CreateView):
    model = Consent
    form_class = ConsentForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        self.request.session['form-submitted'] = True
        message = f"{form.cleaned_data.get('first_name')} {form.cleaned_data.get('last_name')} here is the form you submitted"
        #send_email([form.cleaned_data.get('email')], "Consent Form", message)
        # send_mail(
        #     subject='Consent Form',
        #     message=message,
        #     from_email='contact-form@myapp.com',
        #     recipient_list=[form.cleaned_data.get('email')],
        # )
        return super().form_valid(form)    

class njconsentview(CreateView):
    model = NjConsentData
    form_class = NjConsentForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        self.request.session['form-submitted'] = True
        message = f"{form.cleaned_data.get('first_name')} {form.cleaned_data.get('last_name')} here is the form you submitted"
        # send_email([form.cleaned_data.get('email')], "Consent Form", message)
        # send_mail(
        #     subject='Consent Form',
        #     message=message,
        #     from_email='contact-form@myapp.com',
        #     recipient_list=[form.cleaned_data.get('email')],
        # )
        return super().form_valid(form)

def success(request):
    if not request.session.get('form-submitted', False):
        redirect('consent_form')
    return render(request, "myapp/success.html",{})