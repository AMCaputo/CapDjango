from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def criarconta(request):
    return render(request, 'criarconta.html')

def empresa(request):
    return render(request, 'empresa.html')

def moeda(request):
    return render(request, 'moeda.html')

def bancoempresa(request):
    return render(request, 'bancoempresa.html')

def posto(request):
    return render(request, 'posto.html')

def departamento(request):
    return render(request, 'departamento.html')

def funcao(request):
    return render(request, 'funcao.html')

def funcionario(request):
    return render(request, 'funcionario.html')

def adiantamento(request):
    return render(request, 'adiantamento.html')

def dependente(request):
    return render(request, 'dependente.html')

def avaliacao(request):
    return render(request, 'avaliacao.html')

def formacao(request):
    return render(request, 'formacao.html')

def folhaponto(request):
    return render(request, 'folhaponto.html')

def controlofalta(request):
    return render(request, 'controlofalta.html')

def subsidio(request):
    return render(request, 'subsidio.html')

def outrosubsidio(request):
    return render(request, 'ourosubsidio.html')

def inss(request):
    return render(request, 'inss.html')

def irt(request):
    return render(request, 'irt.html')

def salario(request):
    return render(request, 'salario.html')

def rendimento(request):
    return render(request, 'rendimento.html')

def retencaofonte(request):
    return render(request, 'retencaofonte.html')