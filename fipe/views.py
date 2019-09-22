import re
from .models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response


class CalculaFipe(APIView):
	def get(self,request,*args,**kwargs):
		ano = str(request.GET['ano'])
		modelo = request.GET['modelo']
		modelos = self.busca_modelos(modelo,ano)
		d = self.calcula(modelos)
		return Response(d)

	def busca_modelos(self,veiculo,ano):
		'''
		Busca modelos de veiculos parecidos com o nome passado
		'''
		if '/' in veiculo:
			palavras_chave = veiculo.split('/')
			if palavras_chave[0] == 'I':
					palavras_chave = palavras_chave[1].split(' ')[1:]
			else:
				palavras_chave = palavras_chave[1].split(' ')
			q = Q(marca__icontains=palavras_chave[0])
			print(q)
			modelos = Modelo.objects.filter(q,Q(ano=ano))
			print(modelos)
			m_aux = modelos
			for palavra in palavras_chave[1:]:
				modelos_aux = modelos.filter(marca__icontains=palavra)
				if len(modelos_aux) == 0:
					for word in palavra:
						if word == '':
							continue
						print(word)
						modelos = modelos.filter(marca__icontains=word)
						if len(modelos) != 0:
							m_aux = modelos
						else:
							modelos = m_aux
				else:
					modelos = modelos_aux
			return modelos

	def calcula(self,modelos):
		'''
		Monta o json de resposta com o valor medio
		'''
		if modelos is not None and len(modelos) > 0:
			soma = 0
			i = 0
			d = {'modelos':[]}
			tipo_veiculo = modelos[0].veiculo.marca.tipo_veiculo
			d['provavel_tipo_veiculo'] = tipo_veiculo
			for modelo in modelos:
				d['modelos'].append({
					'modelo':modelo.veiculo.nome,
					'preco':modelo.preco,
					'ano':modelo.ano,
					'tipo_veiculo':modelo.veiculo.marca.tipo_veiculo
				})
				soma += float(modelo.preco[2:].replace('.','').replace(',','.'))
				i += 1
			d['valor_medio'] =  '%.2f' % float(soma/i)
			return d
		else:
			return {'valor_medio':None,'message':'modelo nao encontrado'}
				


# Create your views here.
