from django.urls import path
from .views import AtivoCreate, inicial, AtivoConsulta, AtivoAtualiza, AtivoDeleta

urlpatterns = [
   path('', inicial, name="home"),
   #Ativos
   path('cadastrarativo',           AtivoCreate,   name="cadastra_ativo"),
   path('listarativos',             AtivoConsulta, name="lista_ativos"),
   path('atualizarativo/<int:id>',  AtivoAtualiza, name="atualiza_ativo"),
   path('deletarativo/<int:id>',    AtivoDeleta,   name="deleta_ativo")
   #Local
   ]