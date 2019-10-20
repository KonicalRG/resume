from django.views.generic.edit import CreateView
from .forms import ContactForm


class ContactFormView(CreateView):
    form_class = ContactForm
    template_name = 'partial/_contact.html'
