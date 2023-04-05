from django.contrib import admin

from back.apps.core.models import Collaborator, Departament

# Register your models here.


class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departament', 'created_on', 'updated_on')
    search_fields = ['name', 'email', 'departament', 'created_on', 'updated_on']
    
    
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on')
    search_fields = ['name', 'created_on', 'updated_on']
    
    
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Departament, DepartamentAdmin)