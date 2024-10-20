from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_extensions.routers import ExtendedDefaultRouter

from sku_backend.core.views import LocationViewSet, DepartmentViewSet, CategoryViewSet, SubCategoryViewSet, SKUViewSet


router = ExtendedDefaultRouter()

(
    router.register(r"location", LocationViewSet, basename="location")
    .register(r"department", DepartmentViewSet, basename="location-department", parents_query_lookups=['location'])
    .register(
        r"category",
        CategoryViewSet,
        basename="department-category",
        parents_query_lookups=["department__location", "department"],
    )
    .register(
        r"subcategory",
        SubCategoryViewSet,
        basename="category-subcategory",
        parents_query_lookups=["category__department__location", "category__department", "category"],
    )
    .register(
        r"sku",
        SKUViewSet,
        basename="subcategory-sku",
        parents_query_lookups=[
            "subcategory__category__department__location",
            "subcategory__category__department",
            "subcategory__category",
            "subcategory",
        ],
    )
)


schema_view = get_schema_view(
    openapi.Info(title="sku backend API", default_version="v1"),
    public=True,
    permission_classes=[permissions.AllowAny],
)


app_name = "api"
urlpatterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
] + router.urls
