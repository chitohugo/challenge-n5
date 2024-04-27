from django.contrib import admin

from traffic_violations.models import Person, Vehicle, Make, Model, Infraction, PoliceOfficer


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'dni', 'first_name', 'last_name', 'email', 'created_at')
    search_fields = ('dni', 'first_name', 'email')
    list_filter = ('dni', 'email')
    ordering = ('-created_at',)
    list_per_page = 25


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'patent', 'color', 'make', 'owner', 'created_at')
    search_fields = ('patent', 'color', 'make')
    list_filter = ('patent', 'make', 'owner')
    ordering = ('-created_at',)
    list_per_page = 25


@admin.register(PoliceOfficer)
class OfficialAdmin(admin.ModelAdmin):
    list_display = ('id_official', 'get_first_name', 'get_last_name',)

    # search_fields = ('first_name', 'last_name')
    # list_filter = ('first_name', 'last_name')
    # ordering = ('-created_at', )
    # list_per_page = 25

    def has_add_permission(self, request):
        return False
    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-created_at',)
    list_per_page = 25


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', 'make')
    list_filter = ('name', 'make')
    ordering = ('-created_at',)
    list_per_page = 25


@admin.register(Infraction)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'patent', 'comment', 'created_by', 'created_at')
    search_fields = ('patent', 'created_by')
    list_filter = ('patent',)
    ordering = ('-created_at',)
    list_per_page = 25
