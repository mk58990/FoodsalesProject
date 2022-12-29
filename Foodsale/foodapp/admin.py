from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FoodDetails

# Register your models here.
class FoodDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['OrderDate','Region','City','Category','Product','Quantity','UnitPrice']

admin.site.register(FoodDetails,FoodDetailsAdmin)