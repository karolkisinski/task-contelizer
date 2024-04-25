from django.urls import path
from .views import UploadedFileView


urlpatterns = [
    path('process_text/', UploadedFileView.as_view(), name='process-text'),
]
