from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    # API
    # API usage documentation
    path('', views.index, name='index'),

    # Employee
    # Employee list
    path('api/employees', views.EmployeeListView.as_view(), name='get_employees'),
    # Employee detail
    path('api/employees/<int:pk>', views.EmployeeDetailView.as_view(), name='get_employee'),
    # Employee create
    path('api/employees/create', views.EmployeeCreateView.as_view(), name='create_employee'),

    # Company
    # Company list
    path('api/companies', views.CompanyListView.as_view(), name='get_companies'),
    # Company detail
    path('api/companies/<int:pk>', views.CompanyDetailView.as_view(), name='get_company'),
    # Company create
    path('api/companies/create', views.CompanyCreateView.as_view(), name='create_company'),

    # Position
    # Position list
    path('api/positions', views.PositionListView.as_view(), name='get_positions'),
    # Position detail
    path('api/positions/<int:pk>', views.PositionRUDView.as_view(), name='get_position'),
    # Position create
    path('api/positions/create', views.PositionCreateView.as_view(), name='create_position'),

    # Partnership
    # Partnership list
    path('api/partnerships', views.PartnershipListView.as_view(), name='get_partnerships'),
    # Partnership detail
    path('api/partnerships/<int:pk>', views.PartnershipRUDView.as_view(), name='get_partnership'),
    # Partnership create
    path('api/partnerships/create', views.PartnershipCreateView.as_view(), name='create_partnership'),

    # Templates app
    # Employee
    # Employees page
    path('employees/', views.show_employees, name='employees'),
    # Employee detail page
    path('employee/<int:employee_id>/', views.show_employee, name='employee'),
    # New employee page
    path('new_employee/', views.new_employee, name='new_employee'),
    # Edit employee page
    path('edit_employee/<int:employee_id>', views.edit_employee, name='edit_employee'),
    # Employee deletion
    path('delete_employee/<int:employee_id>', views.delete_employee, name='delete_employee'),
    # Filter by employee position url
    path('filter_by_position/<int:position_id>', views.filtered_employees, name='filtered_employees'),

    # Company
    # Companies page
    path('companies/', views.show_companies, name='companies'),
    # Company detail page
    path('company/<int:company_id>/', views.show_company, name='company'),
    # New company page
    path('new_company/', views.new_company, name='new_company'),
    # Edit company page
    path('edit_company/<int:company_id>', views.edit_company, name='edit_company'),
    # Company deletion
    path('delete_company/<int:company_id>', views.delete_company, name='delete_company'),

    # Position
    # Positions page
    path('positions/', views.show_positions, name='positions'),
    # New position page
    path('new_position/', views.new_position, name='new_position'),
    # Edit position page
    path('edit_position/<int:position_id>', views.edit_position, name='edit_position'),
    # Position deletion
    path('delete_position/<int:position_id>', views.delete_position, name='delete_position'),

    # Partnership
    # Partnerships page
    path('partnerships/', views.show_partnerships, name='partnerships'),
    # New partnership page
    path('new_partnership/', views.new_partnership, name='new_partnership'),
    # Edit partnership page
    path('edit_partnership/<int:partnership_id>', views.edit_partnership, name='edit_partnership'),
    # Partnership deletion
    path('delete_partnership/<int:partnership_id>', views.delete_partnership, name='delete_partnership'),

]
