from django.urls import path
from .views import SubmitCodeView, SubmissionHistoryView

urlpatterns = [
    path("submit/", SubmitCodeView.as_view(), name="submit-code"),
    path("history/<str:username>/", SubmissionHistoryView.as_view(), name="submission-history"),
    
]
