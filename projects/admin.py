from django.contrib import admin

from .models import Portafolio


class PortafolioAdminView(admin.ModelAdmin):
    '''Admin View for Contact '''
    list_display = ('title', 'category', 'author', )
    list_filter = ('title', 'category', 'author', )
    search_fields = ('title', 'category', 'author', )
    ordering = ('title', 'category', 'author',)
    editable_field = ('published')

admin.site.register(Portafolio, PortafolioAdminView)
