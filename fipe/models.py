from django.db import models


# Create your models here.
class Marca(models.Model):
	id = models.CharField(max_length=200,primary_key=True)
	tipo_veiculo = models.CharField(null=True,max_length=1000)
	fipe_name = models.CharField(null=True,max_length=1000)
	nome = models.CharField(null=True,max_length=1000)
	key = models.CharField(null=True,max_length=1000)
	consultado = models.BooleanField()

class Veiculo(models.Model):
	id = models.CharField(max_length=200,primary_key=True)
	marca = models.ForeignKey(Marca,on_delete = models.CASCADE)
	fipe_name = models.CharField(null=True,max_length=1000)
	nome = models.CharField(null=True,max_length=1000)
	key = models.CharField(null=True,max_length=1000)
	consultado = models.BooleanField()

class Modelo(models.Model):
	id1 = models.CharField(max_length=200)
	fipe_codigo = models.CharField(null=True,max_length=1000)
	nome = models.CharField(null=True,max_length=1000)
	key = models.CharField(null=True,max_length=1000)
	marca = models.CharField(null=True,max_length=1000)
	preco = models.CharField(null=True,max_length=1000)
	ano = models.CharField(null=True,max_length=1000)
	consultado = models.BooleanField()	
	veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)