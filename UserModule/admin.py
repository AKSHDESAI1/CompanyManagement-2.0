from django.contrib import admin
from .models import User, Company, Project, Task

# Register your models here.
admin.site.register(User)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'dbaName', 'address',
                    'branch', 'number', 'website', 'fax', 'email']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company', 'name',
                    'description', 'manager', 'supervisor', 'assistants']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company', 'project', 'name',
                    'description', 'manager', 'supervisor', 'assistants']
