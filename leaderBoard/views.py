from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 🟢 Global Leaderboard API
class GlobalLeaderboardView(APIView):
    @swagger_auto_schema(
        operation_summary="Get Global Leaderboard",
        responses={200: "List of top players"},
    )
    def get(self, request):
        leaderboard = [
            {"rank": 1, "username": "Yadhu", "points": 1500},
            {"rank": 2, "username": "Arjun", "points": 1400},
            {"rank": 3, "username": "Sneha", "points": 1350},
        ]
        return Response({"leaderboard": leaderboard}, status=200)


# 🟢 User Rank API
class UserRankView(APIView):
    @swagger_auto_schema(
        operation_summary="Get User Rank",
        responses={200: "User rank details"},
    )
    def get(self, request, username):
        users = {
            "Yadhu": {"rank": 1, "points": 1500},
            "Arjun": {"rank": 2, "points": 1400},
            "Sneha": {"rank": 3, "points": 1350},
        }
        user_data = users.get(username, {"rank": "Unranked", "points": 0})
        return Response({"username": username, "rank": user_data["rank"], "points": user_data["points"]}, status=200)


# 🟢 Recent Wins API
class RecentWinsView(APIView):
    @swagger_auto_schema(
        operation_summary="Get Recent Battle Winners",
        responses={200: "List of recent winners"},
    )
    def get(self, request):
        recent_wins = [
            {"winner": "Arjun", "battle_title": "Dijkstra’s Challenge"},
            {"winner": "Sneha", "battle_title": "Sorting Showdown"},
            {"winner": "Yadhu", "battle_title": "Binary Search Blitz"},
        ]
        return Response({"recent_winners": recent_wins}, status=200)
