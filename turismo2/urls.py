from django.contrib import admin
from django.urls import path
from hotels import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='home'),
	path('signup/', views.signup, name='signup'),
	path('inicio/', views.inicio, name='inicio'),
	path('logout/', views.signout, name='logout'),
	path('signin/', views.signin, name='signin'),
	path('perfil/', views.perfilf, name='perfil'),
	path('departamentos_detail/<str:departamentos_name>/', views.departamentos_detail, name='departamemtos_detail'),
	path('departamentos_detail_hotel/<str:departamentosd_name>/', views.departamentos_detail_hotel, name='departamemtos_detail_hotel'),
	path('hotel_detail/<str:hoteld_name>/', views.hotel_detail, name='hotel_detail'),
	path('createhotel/', views.createhotelf, name='gotel'),
	path('empresarial/', views.empresarial, name='empresarial'),
	path('reservah/', views.reservah, name='reservah'),
	path('reservation/', views.reservation, name='reservation'),
	path('createrest/', views.createrest, name='resta'),
	path('departamentos_detail_rest/<str:departamentosdn_name>/', views.departamentos_detail_rest, name='departamemtos_detail_rest'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
