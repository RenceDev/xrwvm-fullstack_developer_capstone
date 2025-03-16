from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to display CarModels under CarMake in the admin interface
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display for adding CarModel entries by default

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Fields to display in the list view
    list_filter = ('car_make', 'type', 'year')  # Filters to display in the right sidebar
    search_fields = ('name', 'car_make__name')  # Search fields for filtering data
    ordering = ('year',)  # Default ordering of records in the list view

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Fields to display in the list view
    search_fields = ('name',)  # Search field for filtering car makes
    inlines = [CarModelInline]  # Add the CarModelInline to display car models related to the car make

# Registering models with the Django admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
