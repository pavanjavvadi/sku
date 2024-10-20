from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.managers import InheritanceManager
from simple_history.models import HistoricalRecords

User = settings.AUTH_USER_MODEL


class BaseManager(InheritanceManager):
    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    """Base Model
    To be used for Inheriting the fields and following the DRY concept
    """

    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created By"),
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_created",
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        verbose_name=_("Updated By"),
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_updated",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    history = HistoricalRecords(inherit=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    @property
    def _history_user(self):
        return self.created_by

    @_history_user.setter
    def _history_user(self, value):
        self.created_by = value


class Location(BaseModel):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name


class Department(BaseModel):
    location = models.ForeignKey(Location, related_name="departments", on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Category(BaseModel):
    department = models.ForeignKey(Department, related_name="categories", on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name


class SKU(BaseModel):
    sku_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku_name
