from django.urls import path
from .views import ContactFormView

app_name = 'form'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),

]
