from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class perfil(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	movil = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre + '- by ' + self.user.username

class iniciomodel(models.Model):
        titulo = models.CharField(max_length=30)
        description = models.CharField(max_length=10000)
#       email = models.CharField(max_length=30)
        ##image = models.ImageField(upload_to='hotels/images')
        def __str__(self):
                 return self.titulo
class imgmodel(models.Model):
        titulo = models.CharField(max_length=30)
        description = models.CharField(max_length=10000)
#       email = models.CharField(max_length=30)
        image = models.ImageField(upload_to='hotels/images')
        def __str__(self):
                 return self.titulo

class iniciomodelnk(models.Model):
	titulo = models.CharField(max_length=30)
	description = models.CharField(max_length=10000)
#	email = models.CharField(max_length=30)
	image = models.ImageField(upload_to='hotels/images')
	def __str__(self):
		 return self.titulo
class departamentos(models.Model):
	departamento = models.CharField(max_length=30)
	description = models.TextField()
	imageperfil = models.ImageField(upload_to='hotels/images')
	slide = models.ImageField(upload_to='hotels/images')
	slide1 = models.ImageField(upload_to='hotels/images')
	slide2 = models.ImageField(upload_to='hotels/images')
	def __str__(self):
		return self.departamento

class turi(models.Model):
	dep = models.CharField(max_length=30)
	description = models.CharField(max_length=10000)
	#image = models.ImageField(upload_to='hotels/images')
	def __str__(self):
		return self.depi


class hotelesl(models.Model):
	imageperfil = models.ImageField(upload_to='hotels/images')
	slide = models.ImageField(upload_to='hotels/images')
	slide1 = models.ImageField(upload_to='hotels/images')
	slide2 = models.ImageField(upload_to='hotels/images')
	namehotel = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	description = models.TextField()
	numeroDeHabitaciones = models.CharField(max_length=30)
	precio = models.CharField(max_length=30)
	desayuno = models.BooleanField(max_length=30)
#	ciudad = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.namehotel
class reservationhotel(models.Model):
	reservahotel = models.CharField(max_length=30)
	nombrederes = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	date = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.reservahotel + '- by ' + self.user.username


class hotelesp(models.Model):
	imageperfil = models.ImageField(upload_to='hotels/images')
	slide = models.ImageField(upload_to='hotels/images')
	slide1 = models.ImageField(upload_to='hotels/images')
	slide2 = models.ImageField(upload_to='hotels/images')
	namehotel = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	description = models.TextField()
	direccion = models.CharField(max_length=30)
	precio = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.namehotel


class hoteleslni(models.Model):
	namehotel = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	description = models.TextField()
	direccion = models.CharField(max_length=30)
	precio = models.CharField(max_length=30)
	desayuno = models.BooleanField(max_length=30)
#       ciudad = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.namehotel



class reservationhotelx(models.Model):
	reservahotel = models.CharField(max_length=30)
	nombrederes = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)
	reservar_para_el_dia= models.DateField(auto_now=False, auto_now_add=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
 		return self.reservahotel + '- by ' + self.user.username


class restni(models.Model):
	nombre_restaurante = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	descripcion = models.TextField()
	direccion = models.CharField(max_length=30)
	precio = models.CharField(max_length=30)
	desayuno = models.BooleanField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre_restaurante

class departamentosur(models.Model):
        departamento = models.CharField(max_length=30)
        description = models.TextField()
        imageperfil = models.models.CharField(max_length=3000)
        slide = models.models.CharField(max_length=3000)
        slide1 = models.models.CharField(max_length=3000)
        slide2 = models.models.CharField(max_length=3000)
        def __str__(self):
                return self.departamento

