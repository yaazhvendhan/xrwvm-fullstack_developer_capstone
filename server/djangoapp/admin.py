from django.contrib import admin
from .models import CarMake, CarModel

# CarMake Admin
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# CarModel Admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')

# Registering models with admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)



# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
