from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .forms import ContactForm


class ContactFormView(CreateView, SuccessMessageMixin):
    form_class = ContactForm
    template_name = 'partial/_contact.html'
    success_message = "your request was created successfully"
