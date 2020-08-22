from django.contrib import admin

from .models import User, Address

from reversion.admin import VersionAdmin


class UserAdmin(VersionAdmin):
    list_display = ('first_name', 'last_name', 'user_type', 'addresses')
    list_filter = ('first_name',)
    search_fields = ('first_name',)


class AddressAdmin(VersionAdmin):
    list_display = ('street', 'city', 'state', 'zip_code',)
    list_filter = ('zip_code',)
    search_fields = ('street', 'city',)


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)