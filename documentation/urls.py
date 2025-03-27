from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bit War API",
        default_version="v1",
        description="API documentation for Bit War Coding Battle Platform",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="support@bitwar.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("home/", include("home.urls")),
    path("battle/", include("battle.urls")),
    path("leaderboard/", include("leaderBoard.urls")),
    path("submission/", include("submission.urls")),
    path("api/", include("store.urls")),
    path("api/admin/", include("adminpanel.urls")),

    # Swagger URLs
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),

]
