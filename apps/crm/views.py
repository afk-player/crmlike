from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Employee, Company, Position, Partnership
from .forms import EmployeeForm, CompanyForm, PartnershipForm, PositionForm

# Create your views here.


def index(request):
    """CRM homepage"""
    return render(request, 'crm/index.html')


def show_employees(request):
    """Show employees list"""
    employees = Employee.objects.all()
    positions = Position.objects.all()
    context = {'employees': employees, 'positions': positions}
    return render(request, 'crm/employees.html', context)


def filtered_employees(request, position_id):
    """Filter employees by position"""
    position = Position.objects.get(id=position_id)
    employees = Employee.objects.filter(position=position_id)
    context = {'employees': employees, 'position': position}
    return render(request, 'crm/filtered_employees.html', context)


def show_employee(request, employee_id):
    """Show employee details"""
    employee = Employee.objects.get(id=employee_id)
    context = {'employee': employee}
    return render(request, 'crm/employee.html', context)


def delete_employee(request, employee_id):
    """Delete employee from db"""
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('crm:employees')


def show_positions(request):
    """Show positions list"""
    positions = Position.objects.all()
    context = {'positions': positions}
    return render(request, 'crm/positions.html', context)


def new_position(request):
    """Adds new position"""
    if request.method != 'POST':
        form = PositionForm()
    else:
        form = PositionForm(data=request.POST)
        if form.is_valid():
            new_position = form.save(commit=False)
            new_position.save()
            return redirect('crm:positions')

    context = {'form': form}
    return render(request, 'crm/new_position.html', context)


def edit_position(request, position_id):
    """Edit position"""
    position = Position.objects.get(id=position_id)
    if request.method != 'POST':
        form = PositionForm(instance=position)
    else:
        form = PositionForm(data=request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('crm:positions')

    context = {'position': position, 'form': form}
    return render(request, 'crm/edit_position.html', context)


def delete_position(request, position_id):
    """Delete position from db"""
    position = Position.objects.get(id=position_id)
    position.delete()
    return redirect('crm:positions')


def show_partnerships(request):
    """Show partnerships list"""
    partnerships = Partnership.objects.all()
    context = {'partnerships': partnerships}
    return render(request, 'crm/partnerships.html', context)


def edit_partnership(request, partnership_id):
    """Edit partnership"""
    partnership = Partnership.objects.get(id=partnership_id)
    if request.method != 'POST':
        form = PartnershipForm(instance=partnership)
    else:
        form = PartnershipForm(data=request.POST, instance=partnership)
        if form.is_valid():
            form.save()
            return redirect('crm:partnerships')

    context = {'partnership': partnership, 'form': form}
    return render(request, 'crm/edit_partnership.html', context)


def delete_partnership(request, partnership_id):
    """Delete partnership from db"""
    partnership = Partnership.objects.get(id=partnership_id)
    partnership.delete()
    return redirect('crm:partnerships')


def show_companies(request):
    """Show companies list"""
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'crm/companies.html', context)


def show_company(request, company_id):
    """Show company details"""
    employees = Employee.objects.filter(company=company_id)
    employees_to_add = Employee.objects.filter(company=None)
    company = Company.objects.get(id=company_id)
    context = {'company': company, 'employees': employees, 'employees_to_add': employees_to_add}
    return render(request, 'crm/company.html', context)


def delete_company(request, company_id):
    """Delete employee from db"""
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect('crm:companies')


def new_employee(request):
    """Adds new employee"""
    if request.method != 'POST':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.save()
            return redirect('crm:employees')

    context = {'form': form}
    return render(request, 'crm/new_employee.html', context)


def edit_employee(request, employee_id):
    """Edit employee"""
    employee = Employee.objects.get(id=employee_id)
    if request.method != 'POST':
        form = EmployeeForm(instance=employee)
    else:
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('crm:employee', employee_id=employee.id)

    context = {'employee': employee, 'form': form}
    return render(request, 'crm/edit_employee.html', context)


def new_company(request):
    """Adds new company"""
    if request.method != 'POST':
        form = CompanyForm()
    else:
        form = CompanyForm(data=request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.save()
            return redirect('crm:companies')

    context = {'form': form}
    return render(request, 'crm/new_company.html', context)


def edit_company(request, company_id):
    """Edit company"""
    company = Company.objects.get(id=company_id)
    if request.method != 'POST':
        form = CompanyForm(instance=company)
    else:
        form = CompanyForm(data=request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('crm:company', company_id=company.id)

    context = {'company': company, 'form': form}
    return render(request, 'crm/edit_company.html', context)


def new_partnership(request):
    """Adds new partnership"""
    if request.method != 'POST':
        form = PartnershipForm()
    else:
        form = PartnershipForm(data=request.POST)
        if form.is_valid():
            if form.fields['company'] != form.fields['partner']:
                new_partnership = form.save(commit=False)
                new_partnership.save()
                form.save_m2m()
                return redirect('crm:partnerships')
            else:
                return redirect('crm:partnerships')
    context = {'form': form}
    return render(request, 'crm/new_partnership.html', context)