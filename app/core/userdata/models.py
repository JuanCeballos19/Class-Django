from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos
'''
Tipo de datos

agregar verbos_name
registrar el admin.py

CharField = cadena longitud corta
TextField = cadena longitud larga
IntegerField = numero enteros
DateField y DateTimeField =  guardar fecha
EmailField = guarda correo
FileField e ImageField = imagenes
AutoField = se incrementa solo
'''


'----------------------------------------------------------------------------------------------'
# Create your models here.
class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Perfil de Usuario"

        verbose_name_plural = "Perfiles"

    def __str__(self):
       return self.RoleName

'-----------------------------------------------------------------------------------------------'
#tabla de DatosUser
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20, verbose_name = "Identificación")  
    nombUser = models.CharField(max_length = 256, null=True, verbose_name = "Nombre")
    apelUser = models.CharField(max_length = 256, null=True, verbose_name = "Apellidos")
    profeUser = models.CharField(max_length = 100, null=True, verbose_name = "Profesión")
    fotoUser = models.ImageField(default="user.png", verbose_name = "Foto de perfil", upload_to="perfiles/img")
    teleUser = models.CharField(max_length = 20, verbose_name = "Número de telefono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = "Selecciona...", verbose_name = "Género")
    addData = models.DateTimeField(auto_now_add = True, null = True, verbose_name = "Creado el")
    modifiat = models.DateTimeField(auto_now = True, null = True, verbose_name = "Modificado el")

    class Meta:
        verbose_name = "Datos de Usuario"

        verbose_name_plural = "Información"

    def __str__(self): #Cadena para representar el objeto DatosUser (en el sitio de Admin, etc.)
       return self.nombUser





       
'-----------------------------------------------------------------------------------------------'
#tabla de Habilidades
class HabilUser(models.Model):
    NombHabil = models.CharField(max_length = 100)
    DescHabilidad = models.TextField(verbose_name = "Descripcion de la Habilidad")

    class Meta:
        verbose_name = "Habilidades del usuario"

        verbose_name_plural = "Competencias"

    def __str__(self): #Cadena para representar el objeto Habilidades (en el sitio de Admin, etc.)
        return self.NombHabil
'------------------------------------------------------------------------------------------------'
class DetaRoles(models.Model):
    idRol = models.ForeignKey(Roles , on_delete = models.CASCADE, verbose_name ="Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtuser = models.DateTimeField(auto_now = True)
    estaRol = models.CharField(max_length = 10)

    class Meta:
        verbose_name = "Roles de usuarios"

        verbose_name_plural = "Roles"

    def __str__(self):
        return self.idUser
'-----------------------------------------------------------------------------------------------'
class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    pcrHabil = models.DecimalField(max_digits = 2, decimal_places = 1)
    udtHabil = models.DateField(auto_now = True)

    class Meta:
        verbose_name = "Nivel de habilidad"

        verbose_name_plural = "Niveles"

    def __str__(self):
        return self.idUser

'----------------------------------------------------------------------'

