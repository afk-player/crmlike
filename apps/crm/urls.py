from django.urls import path
from . import views


app_name = 'crm'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Filter by employee position url
    path('filter_by_position/<int:position_id>', views.filtered_employees, name='filtered_employees'),
    # Employees page
    path('employees/', views.show_employees, name='employees'),
    # Positions page
    path('positions/', views.show_positions, name='positions'),
    # New position page
    path('new_position/', views.new_position, name='new_position'),
    # Edit position page
    path('edit_position/<int:position_id>', views.edit_position, name='edit_position'),
    # Position deletion
    path('delete_position/<int:position_id>', views.delete_position, name='delete_position'),
    # Employee deletion
    path('delete_employee/<int:employee_id>', views.delete_employee, name='delete_employee'),
    # Partnerships page
    path('partnerships/', views.show_partnerships, name='partnerships'),
    # Companies page
    path('companies/', views.show_companies, name='companies'),
    # Company deletion
    path('delete_company/<int:company_id>', views.delete_company, name='delete_company'),
    # Employee detail page
    path('employee/<int:employee_id>/', views.show_employee, name='employee'),
    # Company detail page
    path('company/<int:company_id>/', views.show_company, name='company'),
    # New employee page
    path('new_employee/', views.new_employee, name='new_employee'),
    # Edit employee page
    path('edit_employee/<int:employee_id>', views.edit_employee, name='edit_employee'),
    # New company page
    path('new_company/', views.new_company, name='new_company'),
    # Edit company page
    path('edit_company/<int:company_id>', views.edit_company, name='edit_company'),
    # New partnership page
    path('new_partnership/', views.new_partnership, name='new_partnership'),
    # Edit partnership page
    path('edit_partnership/<int:partnership_id>', views.edit_partnership, name='edit_partnership'),
    # Partnership deletion
    path('delete_partnership/<int:partnership_id>', views.delete_partnership, name='delete_partnership'),

]
