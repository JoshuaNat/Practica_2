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
	"""Función para obtener la lista de todos los archivos"""
	dirs = os.listdir(path) #Crea una lista de todos los archivos de la ubicación proporcionada
	
	for file in dirs:
		if file.endswith(".txt"): #Si el archivo tiene terminación txt lo añade a una nueva lista
			list.append(Direcciones(file, path)) 
		if "." not in file: #Si el archivo no tiene . significa que es una carpeta
			carpeta = path + "/" +file
			archivos(carpeta) #Asi que la función se llama a si misma con la ubicación de la carpeta

def leer_archivo():
	"""Función para almacenar el contenido de un archivo"""
	for obj in list: #Usando la nueva lista que contiene todos los archivos que nos interesan y su direccion
		filename = obj.ruta + '/' + obj.nombre #Juntamos ambos campos para obtener la direcicón absoluta
		with open(filename) as archivo:
			contenido = archivo.read() #Y leer y almacenar el contenido de los archivos
		nuevo = modificador(contenido) #Mandamos ese contenido a una funcion que hace los cambios solicitados
		crear_archivo(obj.nombre, obj.ruta, nuevo) #Y manda la dirección absoluta y el contenido modificado a una nueva función

def crear_archivo(filename, path, content):
	"""Función para crear nuevos archivos"""
	dir_ori = os.getcwd() #Vemos cual es la dirección donde estamos trabajando
	dir_actual = dir_ori.replace("\\", "/") #Cambiamos las \ por /
	dir_obj = path 

	if dir_actual == dir_obj: #Vemos si la ubicación donde vamos a escribir los archivos es en la que estamos trabajando
		ubicacion = path + '/New ' + filename 
		with open(ubicacion, "w") as archivo: #De ser así solo creamos un archivo nuevo
			archivo.write(content) #Y escribimos el contenido

	else: #De no ser así, significa que estamos dentro de una subcarpeta
		dir_nueva = path + " Copia"
		if not os.path.exists(dir_nueva): #Checamos que no exista ya una copia de la carpeta
			os.makedirs(dir_nueva) #Si no existe la creamos
		ubicacion = path + ' Copia/New ' + filename
		with open(ubicacion, "w") as archivo:
			archivo.write(content) #Y escribimos el contenido en un nuevo archivo

def modificador(texto):
	cadena = ''
	letras = string.ascii_letters[26:] #Letras mayusculas de la A a la Z
	for elem in texto: #Por cada elemento en el texto que recibió
		if elem.isalpha(): #Checa si es caracter o número
			cadena += str(random.randint(0,9)) #Si es caracter lo reemplaza por un numero al azar
		elif elem.isnumeric(): #Si es numero lo reemplaza por una letra al azar
			cadena += random.choice(letras)
		else: #Cualquier otro caso simplemente lo concatena sin mas
			cadena += elem
	return cadena


archivos("C:/Users/xyzna/OneDrive/Escritorio/Practicas SSO/P2")
leer_archivo()

