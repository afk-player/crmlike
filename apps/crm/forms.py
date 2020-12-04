from django import forms

from .models import Employee, Company, Position, Partnership


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'surname', 'gender', 'date_of_birth', 'country', 'email', 'bio', 'employee_photo', 'company',
                  'position')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'country', 'foundation_date')


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = ('company', 'partner')


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('title', )





