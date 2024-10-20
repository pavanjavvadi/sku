from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Location, Department, Category, SubCategory, SKU


class AuditSerializerMixin(serializers.ModelSerializer):
    """
    Mixin to automatically handle created_by and updated_by fields
    in the serializers' create and update methods.
    """

    def create(self, validated_data):
        request = self.context["request"]
        if request and hasattr(request, "user"):
            validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context["request"]
        if request and hasattr(request, "user"):
            validated_data["updated_by"] = request.user
        return super().update(instance, validated_data)


# Serializer for Location
class LocationSerializer(AuditSerializerMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "location_name", "created_by", "updated_by", "created_at", "updated_at"]
        read_only_fields = [
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
        ]


class ReadLocationSerializer(AuditSerializerMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "location_name"]


# Serializer for Department
class DepartmentSerializer(AuditSerializerMixin, ModelSerializer):
    location = ReadLocationSerializer(read_only=True)

    class Meta:
        model = Department
        fields = ["id", "department_name", "location", "created_by", "updated_by", "created_at", "updated_at"]
        read_only_fields = ["location", "created_by", "updated_by", "created_at", "updated_at"]


class ReadDepartmentSerializer(AuditSerializerMixin, ModelSerializer):
    location = ReadLocationSerializer(read_only=True)

    class Meta:
        model = Department
        fields = ["id", "department_name", "location"]


# Serializer for Category
class CategorySerializer(AuditSerializerMixin, ModelSerializer):
    department = ReadDepartmentSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "category_name", "department", "created_by", "updated_by", "created_at", "updated_at"]
        read_only_fields = ["department", "created_by", "updated_by", "created_at", "updated_at"]


class ReadCategorySerializer(AuditSerializerMixin, ModelSerializer):
    department = ReadDepartmentSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "category_name", "department"]


# Serializer for SubCategory
class SubCategorySerializer(AuditSerializerMixin, ModelSerializer):
    category = ReadCategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ["id", "subcategory_name", "category", "created_by", "updated_by", "created_at", "updated_at"]
        read_only_fields = ["created_by", "updated_by", "created_at", "updated_at", "category"]


class ReadSubCategorySerializer(AuditSerializerMixin, ModelSerializer):
    category = ReadCategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ["id", "subcategory_name", "category"]


# Serializer for SKU
class SKUSerializer(AuditSerializerMixin, ModelSerializer):
    subcategory = ReadSubCategorySerializer(read_only=True)

    class Meta:
        model = SKU
        fields = ["id", "sku_name", "subcategory", "created_by", "updated_by", "created_at", "updated_at"]
        read_only_fields = ["created_by", "updated_by", "created_at", "updated_at"]
