from django.urls import path
from .views import PortafolioView, PortafolioDetailView

urlpatterns = [
    path('', PortafolioView.as_view(), name='portafoliolist'),
    path('<int:pk>/', PortafolioDetailView.as_view(), name='portafoliodetail'),
]
