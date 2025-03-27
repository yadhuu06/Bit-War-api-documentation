from django.urls import path
from .views import StoreView, RedeemView,StoreItemDetailView

urlpatterns = [
    path("store/", StoreView.as_view(), name="store"),
    path("store/<int:item_id>/", StoreItemDetailView.as_view(), name="store_item_detail"),
    path("redeem/", RedeemView.as_view(), name="redeem"),
]
