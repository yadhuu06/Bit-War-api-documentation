from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

### ✅ Admin Dashboard (First in Swagger) ###
class QuestionView(APIView):
    """
    Admin Dashboard: Manage Questions API
    """
    @swagger_auto_schema(
        operation_summary="Get All Questions (Admin Dashboard)",
        operation_description="Fetches a list of all available questions.",
        tags=["1️⃣ Admin Dashboard"]
    )
    def get(self, request):
        sample_questions = [
            {"id": 1, "question": "What is Django?"},
            {"id": 2, "question": "Explain REST API."}
        ]
        return Response(sample_questions, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Add a Question (Admin Dashboard)",
        operation_description="Adds a new question from the admin panel.",
        tags=["1️⃣ Admin Dashboard"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description="Question text"),
            },
            required=['question']
        )
    )
    def post(self, request):
        question_text = request.data.get("question", None)
        if not question_text:
            return Response({"error": "Question field is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Question added", "question": question_text}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Edit a Question (Admin Dashboard)",
        operation_description="Updates an existing question.",
        tags=["1️⃣ Admin Dashboard"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description="Updated question text"),
            },
            required=['question']
        )
    )
    def put(self, request, id):
        question_text = request.data.get("question", None)
        if not question_text:
            return Response({"error": "Question field is required"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Question updated", "id": id, "question": question_text}, status=status.HTTP_200_OK)


class TestCaseView(APIView):
    """
    Admin Dashboard: Manage Test Cases API
    """
    @swagger_auto_schema(
        operation_summary="Get All Test Cases (Admin Dashboard)",
        operation_description="Fetches all test cases related to questions.",
        tags=["1️⃣ Admin Dashboard"]
    )
    def get(self, request):
        sample_test_cases = [
            {"id": 1, "question_id": 1, "input": "Hello", "output": "Hello Django"},
            {"id": 2, "question_id": 2, "input": "API", "output": "REST API"}
        ]
        return Response(sample_test_cases, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Add a Test Case (Admin Dashboard)",
        operation_description="Adds a test case to a specific question from the admin panel.",
        tags=["1️⃣ Admin Dashboard"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the question"),
                'input': openapi.Schema(type=openapi.TYPE_STRING, description="Test input"),
                'output': openapi.Schema(type=openapi.TYPE_STRING, description="Expected output"),
            },
            required=['question_id', 'input', 'output']
        )
    )
    def post(self, request):
        question_id = request.data.get("question_id", None)
        input_value = request.data.get("input", None)
        output_value = request.data.get("output", None)

        if not (question_id and input_value and output_value):
            return Response({"error": "All fields (question_id, input, output) are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "message": "Test case added",
            "question_id": question_id,
            "input": input_value,
            "output": output_value
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Edit a Test Case (Admin Dashboard)",
        operation_description="Updates an existing test case.",
        tags=["1️⃣ Admin Dashboard"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question_id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the question"),
                'input': openapi.Schema(type=openapi.TYPE_STRING, description="Updated test input"),
                'output': openapi.Schema(type=openapi.TYPE_STRING, description="Updated expected output"),
            },
            required=['question_id', 'input', 'output']
        )
    )
    def put(self, request, id):
        question_id = request.data.get("question_id", None)
        input_value = request.data.get("input", None)
        output_value = request.data.get("output", None)

        if not (question_id and input_value and output_value):
            return Response({"error": "All fields (question_id, input, output) are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "message": "Test case updated",
            "id": id,
            "question_id": question_id,
            "input": input_value,
            "output": output_value
        }, status=status.HTTP_200_OK)


### ✅ Authentication (Second) ###
class AuthView(APIView):
    @swagger_auto_schema(tags=["2️⃣ Authentication"])
    def post(self, request):
        return Response({"message": "User login"}, status=200)

    @swagger_auto_schema(tags=["2️⃣ Authentication"])
    def post(self, request):
        return Response({"message": "User register"}, status=201)


### ✅ Battle ###
class BattleView(APIView):
    @swagger_auto_schema(tags=["3️⃣ Battle"])
    def post(self, request):
        return Response({"message": "Join Battle"}, status=200)


### ✅ Home ###
class HomeView(APIView):
    @swagger_auto_schema(tags=["4️⃣ Home"])
    def get(self, request):
        return Response({"message": "Get user profile"}, status=200)


### ✅ Leaderboard ###
class LeaderboardView(APIView):
    @swagger_auto_schema(tags=["5️⃣ Leaderboard"])
    def get(self, request):
        return Response({"message": "Get global leaderboard"}, status=200)


### ✅ Submission ###
class SubmissionView(APIView):
    @swagger_auto_schema(tags=["6️⃣ Submission"])
    def get(self, request):
        return Response({"message": "Get user submission history"}, status=200)


### ✅ Redeem (Move to End) ###
class RedeemView(APIView):
    @swagger_auto_schema(tags=["7️⃣ Redeem"])
    def post(self, request):
        return Response({"message": "Redeem a reward"}, status=201)


### ✅ Store (Move to End) ###
class StoreView(APIView):
    @swagger_auto_schema(tags=["8️⃣ Store"])
    def get(self, request):
        return Response({"message": "Get available store items"}, status=200)

    @swagger_auto_schema(tags=["8️⃣ Store"])
    def post(self, request):
        return Response({"message": "Add a new store item"}, status=201)
