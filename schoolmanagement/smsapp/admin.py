from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
@admin.register(schools)
class StudentAdmin(ImportExportModelAdmin):
    pass
@admin.register(login)
class StudentAdmin(ImportExportModelAdmin):
    pass