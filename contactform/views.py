from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from resume.models import AcademicTraining, EmploymentHistory
from .forms import ContactForm


class ContactFormView(CreateView, SuccessMessageMixin):
    form_class = ContactForm
    template_name = 'index.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "your request was created successfully"


