from django.contrib import admin
from .models import Contact


class ContactAdminView(admin.ModelAdmin):
    '''Admin View for Contact '''
    list_display = ('name', 'suject', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email', 'suject')
    ordering = ('name', 'email')


admin.site.register(Contact, ContactAdminView)
