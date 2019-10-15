from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'index.html'
    succes_url = reverse_lazy('index')
