import os
import time
import json
#método para listar archivos
def get_archivos(path):
    print("Obteniendo archivos del directorio local")
    path = path
    data = []
    archivos = os.listdir(path)
    for archivo in archivos:
        a = {'Archivo':archivo}
        data.append(a)
    retjson(data)

def get_tabla(path):
    print("Obteniendo archivos del directorio local")
    path = path
    data=[]
    archivos = os.listdir(path)
    for archivo in archivos:
        a = {'Nombre':archivo, 'Size': os.path.getsize(archivo), 'Fecha_mod': os.path.getmtime(archivo), 'Loc_arch': os.path.abspath(os.getcwd()) }
        data.append(a)
    retjson(data)

#método para obtener el detalle de un archivo seleccionado
def get_detalle(path, archivo):
	data=[]
	a = {'Nombre': archivo, 'Ult_acceso': time.ctime(os.path.getatime(archivo)), 'Fecha_mod': time.ctime(os.path.getmtime(archivo)), 'Size': os.path.getsize(archivo)}
	data.append(a)
	retjson(data)

def retjson(cadena):
	python2json = json.dumps(cadena)
	print(python2json)

#llamadas a los métodos
#get_archivos(".")
#get_detalle(".","paisaje-1.jpg")
#get_tabla(".")