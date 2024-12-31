from django.urls import path
from .views import*


urlpatterns = [
    path('', homepage, name="homepage"),
    path('login/', login, name="login"),
    path('criarconta/', criarconta, name="crearconta"),
    path('moeda/', moeda, name="moeda"),
    path('empresa/', empresa, name="empresa"),
    path('bancoempresa/', bancoempresa, name="bancoempresa"),
    path('posto/', posto, name="posto"),
    path('departamento/', departamento, name="departamento"),
    path('funcao/', funcao, name="funcao"),
    path('funcionario/', funcionario, name="funcionario"),
    path('adiantamento/', adiantamento, name="adiantamento"),
    path('dependente/', dependente, name="dependente"),
    path('avaliacao/', avaliacao, name="avaliacao"),
    path('formacao/', formacao, name="formacao"),
    path('folhaponto/', folhaponto, name="folhaponto"),
    path('controlofalta/', controlofalta, name="controlofalta"),
    path('subsidio/', subsidio, name="subsidio"),
    path('outrosubsidio/', outrosubsidio, name="outrosubsidio"),
    path('inss/', inss, name="inss"),
    path('irt/', irt, name="irt"),
    path('salario/', salario, name="salario"),
    path('rendimento/', rendimento, name="rendimento"),
    path('retencaofonte/', retencaofonte, name="retencaofonte"),
]