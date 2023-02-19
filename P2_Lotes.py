import os, sys

class Direcciones:
	"""Una clase simple para almanecar direcciones y nombres de archivos"""

	def __init__(self, nombre, ruta):
		"""Inicializa los atributos de la clase"""
		self.nombre = nombre
		self.ruta = ruta

#Lista de Direcciones
list = []

def archivos(path):
	dirs = os.listdir(path)
	
	for file in dirs:
		if file.endswith(".txt"):
			list.append(Direcciones(file, path))
		if "." not in file:
			carpeta = path + "/" +file
			archivos(carpeta)




archivos("C:/Users/xyzna/OneDrive/Escritorio/Practicas SSO/P2")

for obj in list:
	print(obj.nombre, obj.ruta, sep=" ")