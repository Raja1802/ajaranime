from django.contrib import admin
from .models import Anime
from import_export.admin import ImportExportModelAdmin


@admin.register(Anime,)
class ViewAdmin(ImportExportModelAdmin):
    pass
