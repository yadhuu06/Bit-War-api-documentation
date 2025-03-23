from django.urls import path
from .views import UserProfileView, SampleQuestionView, QuestionListView, QuestionSearchView

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("sample-question/", SampleQuestionView.as_view(), name="sample-question"),
    path("questions/", QuestionListView.as_view(), name="question-list"),
    path("search/", QuestionSearchView.as_view(), name="question-search"),
]
