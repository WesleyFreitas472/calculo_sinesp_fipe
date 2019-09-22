# SINESP-FIPE

Código fonte de uma API que o valor e o tipo de veiculo da base do SINESP na base tabela FIPE

Sistema hospedado em wesleyfreitas472.pythonanywhere.com

## Exemplo
	```import requests
	r = requests.get(f'http://wesleyfreitas472.pythonanywhere.com/teste?ano=2018&modelo=FIAT/SIENA ATTRACT 1.0')
	print(r.json())
	```

## Retorno
	
	*Veículos de nome e ano parecidos com o passado por parametro
	*Provavel tipo do veículo
	*Valor médio dos veiculos encontrados

	```
	{'modelos': [{'ano': '2018',
		      'modelo': 'Grand Siena ATTRACTIVE 1.0 Flex 8V 4p',
		      'preco': 'R$ 39.189,00',
		      'tipo_veiculo': 'carros'}],
	 'provavel_tipo_veiculo': 'carros',
	 'valor_medio': '39189.00'}
	```

Contribuam com código para a melhoria do projeto!

TODO: Atualizar dados da tabela FIPE.
