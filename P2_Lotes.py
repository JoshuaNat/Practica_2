import os, sys
import random
import string

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

def leer_archivo():
	for obj in list:
		filename = obj.ruta + '/' + obj.nombre
		with open(filename) as archivo:
			contenido = archivo.read()
		nuevo = modificador(contenido)
		crear_archivo(obj.nombre, obj.ruta, nuevo)

def crear_archivo(filename, path, content):
	ubicacion = path + '/New ' + filename 
	with open(ubicacion, "w") as archivo:
		archivo.write(content)


def modificador(texto):
	cadena = ''
	letras = string.ascii_letters[26:]
	for elem in texto:
		if elem.isalpha():
			cadena += str(random.randint(0,9))
		elif elem.isnumeric():
			cadena += random.choice(letras)
		else:
			cadena += elem
	return cadena


archivos("C:/Users/xyzna/OneDrive/Escritorio/Practicas SSO/P2")
leer_archivo()


