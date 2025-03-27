from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Temporary in-memory store items (Replace with DB Model)
store_items = [
    {"item_id": 1, "name": "Premium Badge", "points": 500},
    {"item_id": 2, "name": "Exclusive Avatar", "points": 1000},
]

class StoreView(APIView):
    @swagger_auto_schema(
        operation_summary="Get Available Store Items",
        responses={200: "List of available reward items"},
        tags=["Store"],
    )
    def get(self, request):
        return Response({"items": store_items}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Add a New Store Item",
        tags=["Store"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Item name"),
                "points": openapi.Schema(type=openapi.TYPE_INTEGER, description="Points required"),
            },
            required=["name", "points"],
        ),
        responses={201: "Item added successfully"},
    )
    def post(self, request):
        data = request.data
        new_item = {
            "item_id": len(store_items) + 1,
            "name": data["name"],
            "points": data["points"],
        }
        store_items.append(new_item)
        return Response({"message": "Item added successfully", "item": new_item}, status=status.HTTP_201_CREATED)


class StoreItemDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Edit a Store Item",
        tags=["Store"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Updated item name"),
                "points": openapi.Schema(type=openapi.TYPE_INTEGER, description="Updated points required"),
            },
            required=["name", "points"],
        ),
        responses={200: "Item updated successfully"},
    )
    def put(self, request, item_id):
        for item in store_items:
            if item["item_id"] == item_id:
                item["name"] = request.data.get("name", item["name"])
                item["points"] = request.data.get("points", item["points"])
                return Response({"message": "Item updated successfully", "item": item}, status=status.HTTP_200_OK)
        return Response({"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Delete a Store Item",
        tags=["Store"],
        responses={200: "Item deleted successfully"},
    )
    def delete(self, request, item_id):
        global store_items
        store_items = [item for item in store_items if item["item_id"] != item_id]
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_200_OK)



class RedeemView(APIView):
    @swagger_auto_schema(
        operation_summary="Redeem a Reward",
        tags=["Redeem"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "item_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=["username", "item_id"],
        ),
        responses={200: "Redeem successful", 400: "Not enough points"},
    )
    def post(self, request):
        data = request.data
        # Assume user has enough points (In real case, check from DB)
        return Response({"message": "Redeem successful"}, status=200)
