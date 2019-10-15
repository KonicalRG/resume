from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'suject', 'message')
        widgets = {
            'name' = forms.TextInput(attrs={'size': 35, 'id': 'contactName',
                                            'label': 'Name',
                                            'placeholder':  'Put your name Here'}),

            'suject' = forms.TextInput(attrs={'size': 35,
                                              'id': 'contactSubject',
                                              'label': 'Suject', 'placeholder':  'your matter goes  Here'}),

            'message' = forms.Textarea(attrs={'row': 35, 'col': 50,
                                              'id': 'contactName',
                                              'label': 'Message',
                                              'placeholder': 'your Messae in Here'}),

            'email' = forms.EmailInput(attrs={'id': "contactEmail",
                                              'size': "35", 'label': 'Email',
                                              'placeholder':  'Put your emai Here'}),

        }
