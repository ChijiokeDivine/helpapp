from django.contrib import admin
from .models import WaitlistEmail, Blog, Contact
from django.contrib.auth.models import Group


#unregistered the group model not needed for now
admin.site.unregister(Group)

# admin title 
admin.site.site_header = "HelpAfrica Admin"


# Register your models here.

admin.site.register(WaitlistEmail)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_image','blog_title']
    exclude = ('date','bid')
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)

