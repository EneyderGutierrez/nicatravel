from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib.auth import login, logout, authenticate
from .models import perfil, iniciomodelnk, departamentos, turi, hoteleslni, reservationhotelx as reservationhotel, restni
from .forms import perfilform, createhotel, reservahform, createrestau



# Create your views here.
def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	else:
		if request.POST['contraseña1'] == request.POST['contraseña2']:
			try:
				user =User.objects.create_user(username=request.POST['nombre'],password=request.POST['contraseña1'])
				user.save()
				login(request, user)
				return redirect('inicio')
			except:
					return render(request, 'signup.html',{"error":"el usuario ya existe"})
		return render(request, 'signup.html',{"error":"las contraseñas no coinciden"})

def home(request):
        return render(request, 'home.html')


def inicio(request):
	departamento = departamentos.objects.all()
	#img = imgmodel.objects.all()
#	print (list(img))
	return render(request, 'inicio.html', {'departamentos':departamento})

def signout(request):
	logout(request)
	return redirect('home')

def signin(request):
	if request.method == 'GET':
        	return render(request, 'signin.html')
	else:
		user = authenticate(request,username=request.POST['nombre'],password=request.POST['contraseña'])
		if user is None:
			return render(request,'signin.html',{"error":"Usuario o contraseña incorrectos"})
		else:
			login(request, user)
			return redirect('inicio')
def perfilf(request):
	if request.method == 'GET':
		dataperfil = perfil.objects.filter(user=request.user)
		formperfil = list(dataperfil)
		counp = len(formperfil)
		return render(request,'perfil.html',{'form':perfilform,'perfil':dataperfil, 'lent':counp})
	else:
		dataperfil = perfil.objects.filter(user=request.user)
		formperfil = list(dataperfil)
		counp = len(formperfil)
#		dataperfil = perfil.objects.filter(user=request.user)
		perfilsave = perfilform(request.POST)
		new_perfil = perfilsave.save(commit=False)
		new_perfil.user = request.user
		new_perfil.save()
		return redirect('perfil')

def departamentos_detail(request, departamentos_name):
#	print (departamentos_name)
	departamentod = departamentos.objects.get(departamento = departamentos_name)
	turid = turi.objects.filter(dep = departamentos_name)
#	print (departamentod)
	return render(request, 'departamentos_detail.html',{'departamento_detail':departamentod, 'sites':turid})

def departamentos_detail_hotel(request, departamentosd_name):
#       print (departamentos_name)
	departamentod = departamentos.objects.get(departamento = departamentosd_name)
	hoteld = hoteleslni.objects.filter(ciudad = departamentosd_name)
	return render(request, 'departamentos_detail_hotel.html',{'departamento_detail':departamentod, 'hoteleria':hoteld})


def hotel_detail(request, hoteld_name):
	if request.method == 'GET':
#       print (departamentos_name)                                                                                                     departamentod = departamentos.objects.get(departamento = departamentos_name)
		hoteldetail = hoteleslni.objects.get(namehotel = hoteld_name)
#       print (departamentod)
#

	#print (hoteldetail)
		return render(request, 'hotel_detail.html',{'hoteldet':hoteldetail,'reserva':reservahform})

	else:
		hoteldetail = hoteleslni.objects.get(namehotel = hoteld_name)
		dataperfil = perfil.objects.filter(user=request.user)
	#	reservahformnk = list(datares)
		datares = reservationhotel.objects.filter(user=request.user)
#			reservahform = list(datares)
		#reservahform = list(datares)

		counp = len('data')
		ressave = reservahform(request.POST)
		new_res = ressave.save(commit=False)
		new_res.reservahotel = hoteldetail
		for i in dataperfil:
			print (i.movil)
#		new_res.reservahotel = hoteldetail
			new_res.nombrederes = i.nombre + ' ' + i.apellidos
			new_res.telefono = i.movil
		new_res.user = request.user
		new_res.save()
		return render(request, 'hotel_detail.html',{'hoteldet':hoteldetail,'reserva':reservahform})



#print (hotel_detail(request, hoteld_name))
def createhotelf(request):
	if request.method == 'GET':
		datahotel = hoteleslni.objects.filter(user=request.user)
		for i in datahotel:
			nhotel = i.namehotel
		datares = reservationhotel.objects.filter(reservahotel=nhotel)
		formhotel = list(datahotel)
		counp = len(formhotel)
		return render(request,'createhotel.html',{'form':createhotel,'hotel':datahotel, 'lent':counp, 'datarep':datares})
	else:
		datafhotel = perfil.objects.filter(user=request.user)
		formhotel = list(datafhotel)
		counp = len(formhotel)
		#dataperfil = perfil.objects.filter(user=request.user)
		hotelsave = createhotel(request.POST)

		new_hotel = hotelsave.save(commit=False)
		new_hotel.desayuno = False
		new_hotel.user = request.user
		new_hotel.save()
		return redirect('gotel')



def reservation(request):
# iiiiii      print (departamentos_name)                                                                                            >
#o	hoteldetail = hotelesl.objects.get(namehotel = hoteld_name)
#       print (departamentod)
	return render(request, 'reservaciones.html')



def empresarial(request):
	return render(request, 'empresarial.html')

def reservah(request):
	if request.method == 'Post':
		hoteldetail = hoteleslni.objects.get(namehotel = hoteld_name)
		datares = perfil.objects.filter(user=request.user)
		#reservahform = list(datares)
		counp = len()
		ressave = reservahform(request.POST)
		new_res = ressave.save(commit=False)
		new_res.reservahotel = hoteldetail
		new_res.user = request.user
		print (hoteletail)
#		new_res.save()
		return redirect('gotel')


def createrest(request):
	if request.method == 'GET':
		datahotel = restni.objects.filter(user=request.user)
		formhotel = list(datahotel)
		counp = len(formhotel)
		if counp > 0 :
			for i in datahotel:
				nrest = i.nombre_restaurante
				print (nrest)
				datares = reservationhotel.objects.filter(reservahotel=nrest)
				return render(request,'createrest.html',{'form':createrestau,'hotel':datahotel, 'lent':counp, 'datarep':datares})
#		formhotel = list(datahotel)
#		counp = len(formhotel)ˊ
		else:
			return render(request,'createrest.html',{'form':createrestau,'hotel':datahotel, 'lent':counp})
	else:
		datafhotel = perfil.objects.filter(user=request.user)
		formhotel = list(datafhotel)
		counp = len(formhotel)
                #dataperfil = perfil.objects.filter(user=request.user)
		hotelsave = createrestau(request.POST)

		new_hotel = hotelsave.save(commit=False)
		new_hotel.desayuno = False
		new_hotel.user = request.user
		new_hotel.save()
		return redirect('resta')


def departamentos_detail_rest(request, departamentosdn_name):
#       print (departamentos_name)
	departamentod = departamentos.objects.get(departamento = departamentosdn_name)
	print (departamentod)
	hoteldp = restni.objects.filter(ciudad = departamentosdn_name)
	print (hoteldp)
	return render(request, 'departamentos_detail_rest.html',{'departamento_detail':departamentod, 'restnk':hoteldp})
