import os

def get_archivos(path):
    print("Obteniendo archivos del directorio local")
    path = path
    archivos = os.listdir(path)
    print("[Imprimiendo archivos]")
    for archivo in archivos:
        print(archivo)
    print("[Directorios Mostrados]")
get_archivos(".")
#print(os.name)