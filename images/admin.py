from django.contrib import admin

# Register your models here.
from images.models import File, Tour, Work, Contact


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'passport_number', 'name', 'phone', 'e_mail', 'status', 'created_at')
    list_filter = ("status", 'created_at')
    list_display_links = ['id', 'passport_number']
    list_editable = ['status']
    list_per_page = 15
    search_fields = ['passport_number', 'e_mail', 'phone']
    # prepopulated_fields = {'passport_number': ('passport_number',)}


class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'passport_number', 'name', 'phone', 'e_mail', 'status', 'created_at')
    list_filter = ("status", 'created_at')
    list_display_links = ['id', 'passport_number']
    list_editable = ['status']
    list_per_page = 15
    search_fields = ['passport_number', 'e_mail', 'phone']


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'passport_number', 'name', 'phone', 'e_mail', 'status', 'created_at')
    list_filter = ("status", 'created_at')
    list_display_links = ['id', 'passport_number']
    list_editable = ['status']
    list_per_page = 15
    search_fields = ['passport_number', 'e_mail', 'phone']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'e_mail', 'message', 'status', 'created_at')
    list_filter = ("status", 'created_at')
    list_display_links = ['id', 'name']
    list_editable = ['status']
    list_per_page = 15
    search_fields = ['name', 'e_mail']


admin.site.register(File, StudentAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Contact, ContactAdmin)
