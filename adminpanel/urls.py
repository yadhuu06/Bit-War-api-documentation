from django.urls import path
from .views import QuestionView, TestCaseView

urlpatterns = [
    path('api/questions/', QuestionView.as_view(), name='questions-api'),
    path('api/testcases/', TestCaseView.as_view(), name='testcases-api'),
]
