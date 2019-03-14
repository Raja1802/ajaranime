from django.contrib import admin
from .models import PopularAnime
from import_export.admin import ImportExportModelAdmin


@admin.register(PopularAnime,)
class ViewAdmin(ImportExportModelAdmin):
    pass