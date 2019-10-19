from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm


class ContactFormView(CreateView):
    form_class = ContactForm
    template_name = 'partial/_contact.html'
    succes_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     form.save()
    #     return HttpResponseRedirect(reverse_lazy('contact'))
