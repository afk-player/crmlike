from django import forms
from .models import Employee, Company, Position, Partnership


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = '__all__'

    def clean(self):
        company = self.data['company']
        partnerships = self.data['partner']
        for partner in partnerships:
            if partner == company:
                raise forms.ValidationError("Company can't be partner with itself")
            return self.cleaned_data


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'





