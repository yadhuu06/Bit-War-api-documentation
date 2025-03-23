from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 🟢 Create Battle API
class CreateBattleView(APIView):
    @swagger_auto_schema(
        operation_summary="Create a Coding Battle",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "difficulty": openapi.Schema(type=openapi.TYPE_STRING, enum=["Easy", "Medium", "Hard"]),
            },
            required=["title", "difficulty"],
        ),
        responses={201: "Battle created successfully"},
    )
    def post(self, request):
        return Response({"message": "Battle created successfully"}, status=201)


#  Join Battle API
class JoinBattleView(APIView):
    @swagger_auto_schema(
        operation_summary="Join an Existing Battle",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "battle_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "username": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["battle_id", "username"],
        ),
        responses={200: "Joined battle successfully"},
    )
    def post(self, request):
        return Response({"message": "Joined battle successfully"}, status=200)


#  Submit Solution API
class SubmitSolutionView(APIView):
    @swagger_auto_schema(
        operation_summary="Submit Solution for a Battle",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "battle_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "solution_code": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["battle_id", "solution_code"],
        ),
        responses={200: "Solution submitted successfully"},
    )
    def post(self, request):
        return Response({"message": "Solution submitted successfully"}, status=200)


#  Matchmaking API
class MatchmakingView(APIView):
    @swagger_auto_schema(
        operation_summary="Find an Opponent for a Coding Battle",
        responses={200: "Matched successfully"},
    )
    def get(self, request):
        return Response({"message": "Matched with an opponent!"}, status=200)
