from django import forms
from .models import perfil, hoteleslni ,reservationhotelx as reservationhotel, restni,departamentosur
class perfilform(forms.ModelForm):
        class Meta:
		model = perfil
		fields = ['nombre', 'apellidos','telefono','movil','email','ciudad']
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'movil': forms.TextInput(attrs={'class':'form-control'}),
		}




class createhotel(forms.ModelForm):
	class Meta:
		model = hoteleslni
		fields = ['namehotel','description','ciudad','direccion','precio']
		widgets = {
			'namehotel': forms.TextInput(attrs={'class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
		}






class reservahform(forms.ModelForm):
	class Meta:
		model = reservationhotel
		fields = ['reservar_para_el_dia']
		widgets = {
			'reservar_para_el_dia': forms.DateInput(attrs={'type':'Date'}),
		}


class createrestau(forms.ModelForm):
	class Meta:
		model = restni
		fields = ['nombre_restaurante','descripcion','ciudad','direccion','precio']
		widgets = {
			'nombre_restaurante': forms.TextInput(attrs={'class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
                }

class createdep(forms.ModelForm):
        class Meta:
                model = departamentosur
                fields = ['departamento','description','imageperfil','slide','slide1', 'slide2']
