from django_filters import rest_framework
from .models import Employee


class CharFieldInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class EmployeeFilter(rest_framework.FilterSet):
    position = CharFieldInFilter(field_name='position__title', lookup_expr='in')

    class Meta:
        model = Employee
        fields = ['position', ]
