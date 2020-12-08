from django.contrib import admin
from django.db import models
from .models import Employee, Company, Position, Partnership
from django.forms import CheckboxSelectMultiple


class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Partnership, ForModelAdmin)
