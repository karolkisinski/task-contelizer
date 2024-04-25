from django.urls import path
from .views import PeselValidationView


urlpatterns = [
    path('validate-pesel/', PeselValidationView.as_view(),
         name='validate_pesel'),
]
