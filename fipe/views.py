import re
from .models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response


class CalculaFipe(APIView):
	def get(self,request,*args,**kwargs):
		ano = str(request.GET['ano'])
		modelo = request.GET['modelo']
		a,b,c = self.calcula(modelo,ano)
		
		return Response({'ano':a,'modelo':b,'valor_medio':c})

	def calcula(self,veiculo,ano):
		print('aqui')
		if '/' in veiculo:
			palavras_chave = veiculo.split('/')
			if palavras_chave[0] == 'I':
					palavras_chave = palavras_chave[1].split(' ')
			else:
				palavras_chave = [palavras_chave[0]] + palavras_chave[1].split(' ')

			modelos = Modelo.objects.filter(Q(veiculo__marca__nome__icontains=palavras_chave[0]),
				Q(veiculo__nome__istartswith=palavras_chave[1])
				|Q(veiculo__nome__icontains=re.sub('[^a-zA-Z]','',palavras_chave[1])),Q(ano=ano))
			if len(modelos) == 0:
				#Nao achou o carro com a marca e ano. Procurar o carro sem a marca

				modelos = Modelo.objects.filter(
					Q(veiculo__nome__istartswith=re.sub('[^a-zA-Z]','',palavras_chave[1]))
					|Q(veiculo__nome__icontains=re.sub('[^a-zA-Z]','',palavras_chave[1])),Q(ano=ano))
			for palavra in palavras_chave[1:]:
				for word in palavra:
					m_aux = modelos.filter(veiculo__nome__iregex=word)
					if len(m_aux) != 0:
						modelos = m_aux
			if len(modelos) > 0:
				soma = 0
				i = 1
				tipo_veiculo = modelos[0].veiculo.marca.tipo_veiculo
				for modelo in modelos:
					soma += float(modelo.preco[2:].replace('.','').replace(',','.'))
					i += 1
				return ano,veiculo,soma/i
				
			else:
				return ano,veiculo,'erro'
				


# Create your views here.
