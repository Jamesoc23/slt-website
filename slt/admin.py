from django.contrib import admin
from .models import ContactInfo, Service, About

# Register your models here.

admin.site.register(ContactInfo)
admin.site.register(Service)
admin.site.register(About)
