from django.contrib import admin
from Registration.models import RegistrationStu

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')

admin.site.register(RegistrationStu,SchoolAdmin)
