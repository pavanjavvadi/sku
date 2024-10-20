from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import Location, Department, Category, SubCategory, SKU
from .serializers import (
    LocationSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubCategorySerializer,
    SKUSerializer,
)


# Location ViewSet
class LocationViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# Department ViewSet
class DepartmentViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):

        location_id = self.get_parents_query_dict()["location"]
        location = Location.objects.get(id=location_id)
        serializer.save(location=location)

    def perform_update(self, serializer):
        location_id = self.get_parents_query_dict()["location"]
        location = Location.objects.get(id=location_id)
        serializer.save(location=location)


# Category ViewSet
class CategoryViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        department_id = self.get_parents_query_dict()["department"]
        department = Department.objects.get(id=department_id)
        serializer.save(department=department)

    def perform_update(self, serializer):
        department_id = self.get_parents_query_dict()["department"]
        department = Department.objects.get(id=department_id)
        serializer.save(department=department)


# SubCategory ViewSet
class SubCategoryViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = SubCategory.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        category_id = self.get_parents_query_dict()["category"]
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)

    def perform_update(self, serializer):
        category_id = self.get_parents_query_dict()["category"]
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)


# SKU ViewSet
class SKUViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = SKUSerializer
    permission_classes = [IsAuthenticated]
    queryset = SKU.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        subcategory_id = self.get_parents_query_dict()["subcategory"]
        subcategory = SubCategory.objects.get(id=subcategory_id)
        serializer.save(subcategory=subcategory)

    def perform_update(self, serializer):
        subcategory_id = self.get_parents_query_dict()["subcategory"]
        subcategory = SubCategory.objects.get(id=subcategory_id)
        serializer.save(subcategory=subcategory)
