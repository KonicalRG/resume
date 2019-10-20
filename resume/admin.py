from django.contrib import admin
from .models import EmploymentHistory, AcademicTraining


class EmploymentHistoryAdmin(admin.ModelAdmin):
    '''Admin View for EmploymentHistory '''
    list_display = ('title', 'start_date', 'end_date')
    list_filter = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'start_date', 'end_date')
    ordering = ('title', 'end_date')


class AcadamicTraniningAdmin(admin.ModelAdmin):
    '''Admin View for AcadamicTranining '''
    list_display = ('title', 'college', 'date')
    list_filter = ('title', 'college', 'date')
    search_fields = ('title', 'college', 'date')
    ordering = ('title', 'college', 'date')

admin.site.register(EmploymentHistory, EmploymentHistoryAdmin)
admin.site.register(AcademicTraining, AcadamicTraniningAdmin)
