from django.contrib import admin

from .models import Address,Profile,UserProfileInfo
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    search_fields = ['name','phone','gender']

    list_filter = ['name','phone','gender']

    list_display = ['name','phone','gender']

    list_editable = ['phone']

class AddressAdmin(admin.ModelAdmin):

    search_fields = ['street_address','pin_code']
    list_filter = ['street_address','pin_code']
    list_display = ['street_address','pin_code']
    list_editable = ['pin_code']

admin.site.register(Address,AddressAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserProfileInfo)