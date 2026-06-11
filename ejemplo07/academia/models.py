from django.db import models
import datetime

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()
#     anioNacimiento = models.IntegerField()

# # para la representacion de los objetos 
#     def __str__(self):
#         return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.cedula}  -  Edad: {self.edad} - Año de nacimiento: {self.anioNacimiento}"
    
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.ocultar_ci()}  -  Edad: {self.edad} - Año de nacimiento: {self.obtener_anio()}"
    
    
    def obtener_anio(self):
        anio_actual = datetime.datetime.now().year
        valor = anio_actual - self.edad
        return valor
    
    def ocultar_ci(self):
        ciudad_ci = self.cedula[:2]
        
        if ciudad_ci == "11":
            return "Loja"
        else: 
            return "Otra ciudad"
        