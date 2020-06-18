from django.contrib import admin
# Importamos las clases desde los modelos:

from.models import Roles, DatosUser, HabilUser, DetaRoles, Rates

class RodeModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]
    class Meta:
        model: Roles

admin.site.register(Roles)


class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser"]
    list_display_links = ["nombUser" , "apelUser",]
    
    class Meta:
        model: DatosUser
        
admin.site.register(DatosUser)

class HabilUserModel(admin.ModelAdmin):
    list_display = ["NombHabil"]

    class Meta:
        model: HabilUser

admin.site.register(HabilUser)

class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUser"]

    class Meta:
        model: DetaRoles 
        
admin.site.register(DetaRoles)

class RatesModel(admin.ModelAdmin):
    list_display = ["idUser"]

    class Meta:
        model: Rates 

admin.site.register(Rates)



# Register your models here.
