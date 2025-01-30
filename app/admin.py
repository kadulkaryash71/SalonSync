from django.contrib import admin
from .models import Service, Transaction

# Register your models here.
admin.site.register(Transaction)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'rate')
    ordering = ('date_created', )
    search_fields = ('service_name',)