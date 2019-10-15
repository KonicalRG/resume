from django.urls import path
from .views import ConctacFormView

urlpatterns = [
    path('', ConctacFormView.as_view(), name='contact'),
    
]
