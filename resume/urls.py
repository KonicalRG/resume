from django.urls import path
from contactform.views import ContactFormView
from .views import IndexView


urlpatterns = [path('', IndexView.as_view(), name='index'),
               path('contact/', ContactFormView.as_view(), name='contact'),

               ]
