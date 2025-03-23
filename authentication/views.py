from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserRegisterView(APIView):
    @swagger_auto_schema(
        operation_summary="User Registration",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING, format="email"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format="password"),
            },
            required=["username", "email", "password"],
        ),
        responses={201: "User created successfully"},
    )
    def post(self, request):
        return Response({"message": "User registered successfully"}, status=201)


class UserLoginView(APIView):
    @swagger_auto_schema(
        operation_summary="User Login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, format="email"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format="password"),
            },
            required=["email", "password"],
        ),
        responses={200: "Login successful"},
    )
    def post(self, request):
        return Response({"message": "Login successful"}, status=200)
