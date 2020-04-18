import os
import time
#método para listar archivos

def get_archivos(host,path):
    print("Obteniendo archivos de "+str(host)+"  en la ruta "+str(path))
    path = path
    archivos = os.listdir(path)
    return archivos
#print(os.name)

#método para obtener el detalle de un archivo seleccionado
def get_detalle(path, archivo):
	print("[Detalle del Archivo]")
	print('Nombre del archivo         :', archivo)
	print('Último acceso  :', time.ctime(os.path.getatime(archivo)))
	print('Fecha de Modificación:', time.ctime(os.path.getmtime(archivo)))
	print('Tamaño         :', os.path.getsize(archivo))

#[Lista de archivos]
#archivos = get_archivos(".")
#for archivo in archivos:
#    print(archivo)
