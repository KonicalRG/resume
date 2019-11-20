# resume/views.py

from django.views.generic import TemplateView
from resume.skills import SKILLS
from .models import AcademicTraining, EmploymentHistory


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['academic'] = AcademicTraining.objects.all().order_by('college')
        context['resume'] = EmploymentHistory.objects.all().order_by('-start_date')
        context['skills'] = SKILLS
        return context
