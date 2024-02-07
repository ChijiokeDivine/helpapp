from django.contrib import admin
from .models import WaitlistEmail
# Register your models here.
admin.site.site_header = "HelpAfrica Admin"

admin.site.register(WaitlistEmail)