from django.urls import path
from .views import GlobalLeaderboardView, UserRankView, RecentWinsView

urlpatterns = [
    path("global/", GlobalLeaderboardView.as_view(), name="global-leaderboard"),
    path("user/<str:username>/", UserRankView.as_view(), name="user-rank"),
    path("recent-wins/", RecentWinsView.as_view(), name="recent-wins"),
]
