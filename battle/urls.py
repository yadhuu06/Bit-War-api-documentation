from django.urls import path
from .views import CreateBattleView, JoinBattleView, SubmitSolutionView, MatchmakingView

urlpatterns = [
    path("create/", CreateBattleView.as_view(), name="create-battle"),
    path("join/", JoinBattleView.as_view(), name="join-battle"),
    path("submit/", SubmitSolutionView.as_view(), name="submit-solution"),
    path("matchmaking/", MatchmakingView.as_view(), name="matchmaking"),
]
