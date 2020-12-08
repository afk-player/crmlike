from rest_framework import serializers
from .models import Employee, Company, Position, Partnership


class EmployeeListSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(slug_field='title', read_only=True)
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PartnershipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'

    def validate(self, data):
        company = data['company']
        partnerships = data['partner']
        for partner in partnerships:
            if partner == company:
                raise serializers.ValidationError("Company can't be partner with itself")
            return data


class PartnershipDetailSerializer(serializers.ModelSerializer):
    partner = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Partnership
        fields = '__all__'
