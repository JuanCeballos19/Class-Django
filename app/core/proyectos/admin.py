from django.contrib import admin
from .models import TipoDocu,CategProye,Proyectos,documentos
# Register your models here.

#Registro del modelo de TipoDocu
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombDoc"]
    
    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

#Registro del modelo de CategProye
class CategProyeModel(admin.ModelAdmin):
    list_display = ["lenguaje"]
    
    class Meta:
        model = CategProye
        
admin.site.register(CategProye)

#Registro del modelo de Proyectos
class ProyectosModel(admin.ModelAdmin):
    list_display = ["nombProy"]
    
    class Meta:
        model = Proyectos
        
admin.site.register(Proyectos)

#Registro del modelo de documentos
class documentosModel(admin.ModelAdmin):
    list_display = ["nombDocu"]
    
    class Meta:
        model = documentos
        
admin.site.register(documentos)
