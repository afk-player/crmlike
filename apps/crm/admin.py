from django.contrib import admin
from .models import Employee, Company, Position, Partnership

# Register your models here.


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Partnership)
