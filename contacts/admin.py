from django.contrib import admin
from .models import Contacts
# Register your models here.
#admin.site.register(Contacts)

class ContactsAdmin(admin.ModelAdmin):
    list_display=('name','mobileno')
    ordering=('name',)
    search_fields=('name','mobileno')
admin.site.register(Contacts,ContactsAdmin)