from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
    
class Moeda(models.Model):
	DescricaoMoeda = models.CharField(max_length=150, null=True, blank=True)
	AbreviacaoMoeda = models.CharField(max_length=150, null=True, blank=True)
	Cambio = models.DecimalField(max_digits=10, decimal_places=2)
	
class Empresa(models.Model):
    logo_empresa = models.ImageField(upload_to='thumb_logo', blank=True)
    DecricaoEmpresa = models.CharField(max_length=200, null=True, blank=True)
    NifEmpresa = models.CharField(max_length=50, null=True, blank=True)
    InssEmpresa = models.IntegerField(default=0)
    Provincia = models.CharField(max_length=100, null=True, blank=True)
    Municipio = models.CharField(max_length=100, null=True, blank=True)
    CelularEmpresa = models.CharField(max_length=50, null=True, blank=True)
    FixoEmpresa = models.CharField(max_length=50, null=True, blank=True)
    EmailEmpresa = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    IdMoeda = models.ForeignKey(Moeda, null=True, blank=True, on_delete=models.SET_NULL)

class BancoEmpresa(models.Model):
	DescriacaoBanco = models.CharField(max_length=150, null=True, blank=True)
	ContaEmpresa = models.CharField(max_length=50, null=True, blank=True)
	IbanEmprea = models.CharField(max_length=50, null=True, blank=True)
	IdEmpresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)

class Posto(models.Model):
    DescricaoPosto = models.CharField(max_length=150, null=True, blank=True)
    Provincia = models.CharField(max_length=100, null=True, blank=True)
    Municipio = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    IdEmpresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)

class Departamento(models.Model):
	DescricaoDepartamento = models.CharField(max_length=150, null=True, blank=True)
	AbreviacaoDepartamento = models.CharField(max_length=50, null=True, blank=True)

class Funcao(models.Model):
	DescricaoFuncao = models.CharField(max_length=150, null=True, blank=True)
	AbreviacaoFuncao = models.CharField(max_length=50, null=True, blank=True)

class Funcionario(models.Model):
    nomefuncionario = models.CharField(max_length=50, null=True, blank=True)
    NumeroFuncionrio = models.CharField(max_length=200, null=True, blank=True)
    NifFuncionario = models.CharField(max_length=50, null=True, blank=True)
    DataNascimento = models.DateTimeField(default=timezone.now)
    DataContratacao = models.DateTimeField(default=timezone.now)
    Salariobasico = models.DecimalField(max_digits=10, decimal_places=2)
    ContaBancaria = models.CharField(max_length=50, null=True, blank=True)
    IbanFuncionario = models.CharField(max_length=50, null=True, blank=True)
    InssFuncionario = models.IntegerField(default=0)
    Provincia = models.CharField(max_length=100, null=True, blank=True)
    Municipio = models.CharField(max_length=100, null=True, blank=True)
    CelularFuncionario = models.CharField(max_length=50, null=True, blank=True)
    FixoFuncionario = models.CharField(max_length=50, null=True, blank=True)
    EmailFuncionario = models.CharField(max_length=150, null=True, blank=True)
    IdDepartamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    IdFuncao = models.ForeignKey(Funcao, null=True, blank=True, on_delete=models.SET_NULL)
    IdEmpresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)
    IdMoeda = models.ForeignKey(Moeda, null=True, blank=True, on_delete=models.SET_NULL)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

class AdiantamentoSalario(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DataAdiantamento = models.DateTimeField(default=timezone.now)
	ValorAdiantamento = models.DecimalField(max_digits=10, decimal_places=2)
	Prestacao = models.DecimalField(max_digits=10, decimal_places=2)
	DataInicio = models.DateTimeField(default=timezone.now)
	DataFim = models.DateTimeField(default=timezone.now)


class Dependente(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DescricaoDependente = models.CharField(max_length=150, null=True, blank=True)
	NumeroDocumento = models.CharField(max_length=100, null=True, blank=True)
	GraoParentesco = models.CharField(max_length=50, null=True, blank=True)
	DataNascimento = models.DateTimeField(default=timezone.now)

class Avaliacao(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DescricaoAvaliacao = models.CharField(max_length=200, blank=True, null=True)
	IdDepartamento = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	DataAvaliacao = models.DateTimeField(default=timezone.now)
	Pontuacao = models.IntegerField(default=0)
	Observacao = models.CharField(max_length=200, null=True, blank=True)

class Formacao(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DescricaoFormacao = models.CharField(max_length=200, blank=True, null=True)
	IdDepartamento = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	DataFormacao = models.DateTimeField(default=timezone.now)
	Pontuacao = models.IntegerField(default=0)
	Observacao = models.CharField(max_length=200, null=True, blank=True)
	

class FolhaPonto(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DataPonto = models.DateTimeField(default=timezone.now)
	IdDepartamento = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	HoraEntrada = models.TimeField(default=timezone.now)
	HoraSaida = models.TimeField(default=timezone.now)
	

class ControloFalta(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	DataFalta = models.DateTimeField(default=timezone.now)
	Quantidadefalta = models.IntegerField(default=0)
	

class PlanoFeria(models.Model):
	Observacao = models.CharField(max_length=200, null=True, blank=True)
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	AnoFeria = models.IntegerField(default=0)
	DataInicioFeria = models.DateTimeField(default=timezone.now)
	DataFinalFeria = models.DateTimeField(default=timezone.now)
	ValorFeria = models.DecimalField(max_digits=10, decimal_places=2)
	DiaFeria = models.IntegerField(default=0)
	IdFalta = models.ForeignKey(ControloFalta, blank=True, null=True, on_delete=models.SET_NULL)
	

class Subsidio(models.Model):
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	Alimentacao = models.DecimalField(max_digits=10, decimal_places=2)
	Transporte = models.DecimalField(max_digits=10, decimal_places=2)
	Familia = models.DecimalField(max_digits=10, decimal_places=2)
	Assidiedade = models.DecimalField(max_digits=10, decimal_places=2)
	Outros = models.DecimalField(max_digits=10, decimal_places=2)
	
class OutrosSubsidio(models.Model):
	idfuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	Ferias = models.DecimalField(max_digits=10, decimal_places=2)
	HorasExtra = models.DecimalField(max_digits=10, decimal_places=2)
	DessimoTerceiro = models.DecimalField(max_digits=10, decimal_places=2)
	TresPorcento = models.DecimalField(max_digits=10, decimal_places=2)

class MovimentoInss(models.Model):
	IdEmpresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.SET_NULL)
	DataMovimento = models.DateTimeField(default=timezone.now)
	MesMovimento = models.CharField(max_length=30, null=True, blank=True)
	AnoMovimento = models.IntegerField(default=0)
	TotalIliquido = models.DecimalField(max_digits=10, decimal_places=2)
	TotalInss = models.DecimalField(max_digits=10, decimal_places=2)

class InssItem(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	InssFuncionario = models.IntegerField(default=0)
	Salariobasico = models.DecimalField(max_digits=10, decimal_places=2)
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	Idoutro = models.ForeignKey(OutrosSubsidio, blank=True, null=True, on_delete=models.SET_NULL)
	tresPorcento = models.DecimalField(max_digits=10, decimal_places=2)
	OitoPorcento = models.DecimalField(max_digits=10, decimal_places=2)
	TresPorcentoReformado = models.DecimalField(max_digits=10, decimal_places=2)
	OitoPorcentoReformado = models.DecimalField(max_digits=10, decimal_places=2)
	OnzePorcento = models.DecimalField(max_digits=10, decimal_places=2)
	

class Rendimento(models.Model):
	Escalao = models.CharField(max_length=10, null=True, blank=True)
	ValorUm = models.DecimalField(max_digits=10, decimal_places=2)
	ValorDois = models.DecimalField(max_digits=10, decimal_places=2)
	ParcelaFixa = models.DecimalField(max_digits=10, decimal_places=2)
	Taxa = models.IntegerField(default=0)
	Excesso = models.DecimalField(max_digits=10, decimal_places=2)

class MovimentoIrt(models.Model):
	IdEmpresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.SET_NULL)
	DataMovimento = models.DateTimeField(default=timezone.now)
	MesMovimento = models.CharField(max_length=20, null=True, blank=True)
	AnoMovimento = models.IntegerField(default=0) 
	TotalLiquido = models.DecimalField(max_digits=10, decimal_places=2)

class IrtItem(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL)
	Idsubsidio = models.ForeignKey(Subsidio, blank=True, null=True, on_delete=models.SET_NULL)
	Idoutro = models.ForeignKey(OutrosSubsidio, blank=True, null=True, on_delete=models.SET_NULL)
	BaseIrt = models.DecimalField(max_digits=10, decimal_places=2)
	IdRendimento = models.ForeignKey(Rendimento, blank=True, null=True, on_delete=models.SET_NULL)
	Taxa = models.DecimalField(max_digits=10, decimal_places=2)
	Excesso = models.DecimalField(max_digits=10, decimal_places=2)

class MovimentoSalario(models.Model):
	IdEmpresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.SET_NULL) 
	DataMovimento = models.DateTimeField(default=timezone.now)
	MesMovimento = models.CharField(max_length=20, null=True, blank=True)
	AnoMovimento = models.IntegerField(default=0) 
	TotalSalario = models.DecimalField(max_digits=10, decimal_places=2) 
	TotalSubsidio = models.DecimalField(max_digits=10, decimal_places=2) 
	TotatInss = models.DecimalField(max_digits=10, decimal_places=2) 
	TotalIrt = models.DecimalField(max_digits=10, decimal_places=2)

class SalarioItem(models.Model):
	IdFuncionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL) 
	ContaBancario = models.CharField(max_length=30, null=True, blank=True)
	Salariobasico = models.DecimalField(max_digits=10, decimal_places=2) 
	IdFuncao = models.ForeignKey(Funcao, blank=True, null=True, on_delete=models.SET_NULL) 
	Idsubsidio = models.ForeignKey(Subsidio, blank=True, null=True, on_delete=models.SET_NULL) 
	Idoutro = models.ForeignKey(OutrosSubsidio, blank=True, null=True, on_delete=models.SET_NULL) 
	Iliquido = models.DecimalField(max_digits=10, decimal_places=2) 
	IdAdiantamento = models.ForeignKey(AdiantamentoSalario, blank=True, null=True, on_delete=models.SET_NULL) 
	IdFalta = models.ForeignKey(FolhaPonto, blank=True, null=True, on_delete=models.SET_NULL) 
	IdInss = models.ForeignKey(MovimentoInss, blank=True, null=True, on_delete=models.SET_NULL) 
	IdIrt = models.ForeignKey(MovimentoIrt, blank=True, null=True, on_delete=models.SET_NULL) 
	Liquido = models.DecimalField(max_digits=10, decimal_places=2) 
	

class RetencaoFonte(models.Model):
	nome = models.CharField(max_length=200, blank=True, null=True)
	nif = models.CharField(max_length=50, null=True, blank=True)
	numerofactura = models.CharField(max_length=50, blank=True, null=True)
	data = models.DateTimeField(default=timezone.now)
	valor = models.DecimalField(decimal_places=2, max_digits=10)
	
