from django.contrib import admin
from .models import Episode
from import_export.admin import ImportExportModelAdmin


@admin.register(Episode,)
class ViewAdmin(ImportExportModelAdmin):
    pass
