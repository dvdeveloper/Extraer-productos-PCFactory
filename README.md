# Extractor de productos - PCFactory
Script para extraer productos por categoría de PCFactory (https://www.pcfactory.cl) y guardar el resultado en un excel

[Descargar ejemplo excel](https://github.com/dvdeveloper/Extraer-productos-PCFactory/blob/master/pcfactory.xls?raw=true)
# Dependencias Python 3

BeautifulSoup4
```python
pip3 install BeautifulSoup4
```
HTTP Lib
```python
pip3 install httplib2
```
Python Excel xlwt
```python
pip3 install xlwt
```

Ejemplo array categorias
```python
Categorias	 = [("Discos Externos","https://www.pcfactory.cl/?categoria=422&papa=706"),
				("Desktops","https://www.pcfactory.cl/?categoria=626&papa=737"),
				("Tarjetas Gráficas NVIDIA","https://www.pcfactory.cl/?categoria=378&papa=334"),
				("Tarjetas Gráficas AMD","https://www.pcfactory.cl/?categoria=454&papa=334"),
				("CPU AMD sAM3+","https://www.pcfactory.cl/?categoria=499&papa=272"),
				("Monitores LCD y LED","https://www.pcfactory.cl/?categoria=250&papa=256"),
				("Refrigeración CPU","https://www.pcfactory.cl/?categoria=648&papa=42"),
				("Tablets","https://www.pcfactory.cl/?categoria=488&papa=735")]
```


