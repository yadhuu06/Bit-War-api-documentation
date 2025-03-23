from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 🟢 Profile API
class UserProfileView(APIView):
    @swagger_auto_schema(
        operation_summary="Fetch User Profile",
        responses={200: "User profile details"},
    )
    def get(self, request):
        return Response({"username": "Yadhu", "email": "yadhu@example.com"}, status=200)


# 🟢 Sample Question API
class SampleQuestionView(APIView):
    @swagger_auto_schema(
        operation_summary="Get Sample Coding Question",
        responses={200: "Sample coding question"},
    )
    def get(self, request):
        return Response({"question": "Reverse a string", "difficulty": "Easy"}, status=200)


# 🟢 List All Questions API
class QuestionListView(APIView):
    @swagger_auto_schema(
        operation_summary="Get List of All Coding Questions",
        responses={200: "List of questions"},
    )
    def get(self, request):
        questions = [
            {"id": 1, "title": "Reverse a string", "difficulty": "Easy"},
            {"id": 2, "title": "Find Prime Numbers", "difficulty": "Medium"},
            {"id": 3, "title": "Dijkstra's Algorithm", "difficulty": "Hard"},
        ]
        return Response({"questions": questions}, status=200)


# 🟢 Search Question API
class QuestionSearchView(APIView):
    @swagger_auto_schema(
        operation_summary="Search Coding Questions",
        manual_parameters=[
            openapi.Parameter(
                "query", openapi.IN_QUERY, description="Search term", type=openapi.TYPE_STRING
            )
        ],
        responses={200: "Search results"},
    )
    def get(self, request):
        search_query = request.GET.get("query", "").lower()
        questions = [
            {"id": 1, "title": "Reverse a string", "difficulty": "Easy"},
            {"id": 2, "title": "Find Prime Numbers", "difficulty": "Medium"},
            {"id": 3, "title": "Dijkstra's Algorithm", "difficulty": "Hard"},
        ]
        filtered_questions = [q for q in questions if search_query in q["title"].lower()]
        return Response({"results": filtered_questions}, status=200)
