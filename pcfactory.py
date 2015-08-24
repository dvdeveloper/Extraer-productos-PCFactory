from bs4 import BeautifulSoup
import urllib.request
import re
import operator

import xlwt
from tempfile import TemporaryFile

def ordenPaginador(paginas):
	paginas 	= list(set(paginas))
	list_pag 	= list()
	for p in paginas:
		try:
			num = int(p.text)
			list_pag.append(num)
		except:
			pass
	list_pag.append(1)
	return sorted(list_pag)

def extraerCategoria(urlCategoria,nombre_hoja_excel):

	sheet1 		= book.add_sheet(nombre_hoja_excel)
	url 		= urlCategoria
	page 		= urllib.request.urlopen(url)

	soup 		= BeautifulSoup(page.read(),'html.parser')
	content 	= soup.find('div',{'id':'center'})
	productos 	= content.findAll('span', {"class":["precioGrupo", "nombre_corto"]})
	paginas 	= content.findAll('a',{"class":["nav_sublink_nuevo"]})

	columna = 0
	fila = 0

	paginas 	= ordenPaginador(paginas)
	for pag in paginas:

		url 		= urlCategoria +"&pagina={}".format(pag)
		page 		= urllib.request.urlopen(url)

		soup 		= BeautifulSoup(page.read(),'html.parser')
		content 	= soup.find('div',{'id':'center'})
		productos 	= content.findAll('span', {"class":["precioGrupo", "nombre_corto"]})

		total_columna = 1;
		count = 0
		for p in productos:
			html = BeautifulSoup(str(p),'html.parser')
			texto = html.text;

			if columna == 1:
				texto = texto.replace('$','')
				texto = texto.replace('.','')
				texto = int(texto)

			sheet1.write(fila,columna,texto)

			if total_columna == columna:
				columna = 0
				fila += 1
			else:
				columna +=1

Categorias	 = [("Discos Externos","https://www.pcfactory.cl/?categoria=422&papa=706"),
				("Desktops","https://www.pcfactory.cl/?categoria=626&papa=737"),
				("Tarjetas Gráficas NVIDIA","https://www.pcfactory.cl/?categoria=378&papa=334"),
				("Tarjetas Gráficas AMD","https://www.pcfactory.cl/?categoria=454&papa=334"),
				("CPU AMD sAM3+","https://www.pcfactory.cl/?categoria=499&papa=272"),
				("Monitores LCD y LED","https://www.pcfactory.cl/?categoria=250&papa=256"),
				("Refrigeración CPU","https://www.pcfactory.cl/?categoria=648&papa=42"),
				("Tablets","https://www.pcfactory.cl/?categoria=488&papa=735")]
book = xlwt.Workbook()

total 		 = len(Categorias)
count 		 = 1;
for Key,Value in Categorias:
	print("Páginas extraidas {0} de {1},por favor espere...".format(count,total))
	extraerCategoria(Value,Key)
	count = count+1

name = "pcfactory.xls"
book.save(name)
book.save(TemporaryFile())