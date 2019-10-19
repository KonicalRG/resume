from django.views.generic import TemplateView
from contactform.forms import ContactForm
from .models import AcademicTraining, EmploymentHistory


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['academic'] = AcademicTraining.objects.all().order_by('-date')
        context['resume'] = EmploymentHistory.objects.all().order_by('-end_date')
        context['form'] = ContactForm
        return context
