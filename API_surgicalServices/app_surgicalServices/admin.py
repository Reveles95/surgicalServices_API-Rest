from django.contrib import admin
from .models import *

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_Name', 'service_Description', 'mail', 'team')

class specialistsTeamAdmin(admin.ModelAdmin):
    list_display = ('Name','Last_Name','Expertise','Gender','About','specialist_Services','Adress', 'Edu','fk_Services')

admin.site.register(Services, ServiceAdmin)
admin.site.register(specialistsTeam, specialistsTeamAdmin)
