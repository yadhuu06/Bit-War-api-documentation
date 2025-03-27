from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Temporary storage for submissions (Ideally, store in the database)
submissions = []

# 🟢 Submit Code API
class SubmitCodeView(APIView):
    @swagger_auto_schema(
        operation_summary="Submit Code for Evaluation",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "question_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "language": openapi.Schema(type=openapi.TYPE_STRING),
                "code": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["username", "question_id", "language", "code"],
        ),
        responses={201: "Submission successful"},
    )
    def post(self, request):
        data = request.data
        # Simulate test case execution (in real case, run in a secure sandbox)
        test_case_passed = "print('Hello World')" in data["code"]
        result = "Passed" if test_case_passed else "Failed"

        # Store submission (replace this with database storage)
        submissions.append({
            "username": data["username"],
            "question_id": data["question_id"],
            "language": data["language"],
            "code": data["code"],
            "result": result
        })
        
        return Response({"message": "Submission successful", "result": result}, status=201)


# 🟢 Submission History API
class SubmissionHistoryView(APIView):
    @swagger_auto_schema(
        operation_summary="Get User Submission History",
        responses={200: "List of past submissions"},
    )
    def get(self, request, username):
        user_submissions = [s for s in submissions if s["username"] == username]
        return Response({"username": username, "submissions": user_submissions}, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StoreView(APIView):
    @swagger_auto_schema(
        operation_summary="Get Available Store Items",
        responses={200: "List of available reward items"},
    )
    def get(self, request):
        store_items = [
            {"item_id": 1, "name": "Premium Badge", "points": 500},
            {"item_id": 2, "name": "Exclusive Avatar", "points": 1000},
        ]
        return Response({"items": store_items}, status=200)


