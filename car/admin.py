from django.contrib import admin
from .models import Company, Cars

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display=['title','company','photo']
    prepopulated_fields={'slug':('title',)}