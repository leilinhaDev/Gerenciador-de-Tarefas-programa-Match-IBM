from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionarTarefa', views.adicionarTarefa, name='adicionarTarefa'),
    path('deletarTarefa/<int:id>', views.deletarTarefa, name='deletarTarefa'),
    path('mudarTarefa/<int:id>', views.mudarTarefa, name='mudarTarefa')
   
]