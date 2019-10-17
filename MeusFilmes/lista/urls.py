from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar', views.cadastrar , name='cadastrar'),
    path('deletar', views.deletar , name='deletar'),
    path('modificar', views.modificar , name='modificar'),
    path('vistos', views.visto, name='vistos')
]
