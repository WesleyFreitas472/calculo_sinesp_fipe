
from colorama import Fore, Back, Style
import json
import requests
import pprint


linhas = [
	['2012','HONDA/CG150 FAN ESDI'],
	['2012','M.BENZ/INDUSCAR APACHE U'],
	['2012','KAWASAKI/VERSYS ABS'],
	['2012','CHEVROLET/CELTA 1.0L LS'],
	['2012','I/CITROEN C4 PALLAS20GAF'],
	['2012','RENAULT/LOGAN EXP 16'],
	['2012','HONDA/CG 150 FAN ESI'],
	['2012','VW/FOX 1.0 GII'],
	['2012','FIAT/STRADA WORKING'],
	['2012','FIAT/STRADA ADVENT FLEX'],
	['2012','GM/ZAFIRA ELITE'],
	['2012','I/RENAULT FLUENCE DYN20M'],
	['2012','FORD/FIESTA FLEX'],
	['2012','CHEVROLET/MONTANA LS'],
	['2012','HONDA/BIZ 125 EX'],
	['2012','FIAT/SIENA EL FLEX'],
	['2012','I/VW JETTA 2.0'],
	['2012','CHEVROLET/MONTANA LS'],
	['2012','I/CITROEN C4 PALLAS20GAF'],
	['2012','VW/GOL 1.0'],
]


for linha in linhas:
	r = requests.get(f'http://localhost:8000/consulta?ano={linha[0]}&modelo={linha[1]}')
	print(Fore.RED + linha[0],Fore.RED + linha[1])
	print(Style.RESET_ALL)
	pprint.pprint(r.json())
